# PsGetParentSilo

- RVA: `0x00A70760`–`0x00A7077F` (길이 `31` bytes)
- VA: `0x0000000140A70760`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `10`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A70770` → [PspGetJobSilo](../../text/41/PspGetJobSilo_function_00418670.md) (function, `0x00418670`)

### Direct callers
- [PspConvertSiloToServerSilo](../77/PspConvertSiloToServerSilo_function_0077F9B4.md) at `0x0077FAB5`
- [ObCreateSiloRootDirectory](../83/ObCreateSiloRootDirectory_function_0083CA34.md) at `0x0083CAB8`
- [ObCreateSiloRootDirectory](../83/ObCreateSiloRootDirectory_function_0083CA34.md) at `0x0083CAD7`
- [ObGetSiloRootDirectoryPath](../83/ObGetSiloRootDirectoryPath_function_0083CD74.md) at `0x0083CDD1`
- [IopParseDevice](../89/IopParseDevice_function_0089E510.md) at `0x0089FD19`
- [VRegEnabledInJob](../93/VRegEnabledInJob_function_009350B0.md) at `0x00935109`
- [sub_00B316B4](../B3/Unknown_function_00B316B4.md) at `0x00B32114`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A70770` → [PspGetJobSilo](../../text/41/PspGetJobSilo_function_00418670.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A70760  48 83 EC 28                     sub rsp, 0x28
00A70764  48 85 C9                        test rcx, rcx
00A70767  74 12                           je 0x140a7077b
00A70769  48 8B 89 18 05 00 00            mov rcx, qword ptr [rcx + 0x518]
00A70770  E8 FB 7E 9A FF                  call 0x140418670
00A70775  48 83 C4 28                     add rsp, 0x28
00A70779  C3                              ret
00A7077A  CC                              int3
00A7077B  33 C0                           xor eax, eax
00A7077D  EB F6                           jmp 0x140a70775
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetParentSilo(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 == 0) goto loc_00A7077B;
    result = PspGetJobSilo(*(unsigned __int64 *)(a1 + 1304), a2, a3, a4);
loc_00A70775:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A7077B:
    result = 0;
    goto loc_00A70775;
}
```

## 5. (Beta) C Style

```c
int64_t PsGetParentSilo(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == 0) goto loc_00A7077B;
    result = PspGetJobSilo(*(uint64_t *)(Arg1 + 0x518), a2, a3, a4);
loc_00A70775:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A7077B:
    result = 0;
    goto loc_00A70775;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A70760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A70760[BB_00A70760]
  bb_00A70769[BB_00A70769]
  bb_00A70775[BB_00A70775]
  bb_00A7077A[BB_00A7077A]
  bb_00A7077B[BB_00A7077B]
  bb_00A70760 -->|branch| bb_00A7077B
  bb_00A70760 -->|fallthrough| bb_00A70769
  bb_00A70769 -->|flow| bb_00A70775
  bb_00A7077A -->|flow| bb_00A7077B
  bb_00A7077B -->|branch| bb_00A70775
```
