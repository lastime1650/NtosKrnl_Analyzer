# DbgkpResumeProcess

- RVA: `0x00A7954C`–`0x00A79566` (길이 `26` bytes)
- VA: `0x0000000140A7954C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A79556` → [PsThawMultiProcess](../../text/45/PsThawMultiProcess_function_0045FFE0.md) (function, `0x0045FFE0`)
- `0x00A7955B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [sub_006F88AE](../../text/6F/Unknown_function_006F88AE.md) at `0x006F8ACB`
- [DbgkpSendApiMessageLpc](../92/DbgkpSendApiMessageLpc_function_00920E4C.md) at `0x00920F44`
- [DbgkpSendErrorMessage](../92/DbgkpSendErrorMessage_function_009210A8.md) at `0x00921510`
- [DbgkpSendErrorMessage](../92/DbgkpSendErrorMessage_function_009210A8.md) at `0x00921552`
- [DbgkpSendApiMessage](DbgkpSendApiMessage_function_00A79458.md) at `0x00A794ED`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A79556` → [PsThawMultiProcess](../../text/45/PsThawMultiProcess_function_0045FFE0.md) (`PAGE` → `.text`)
  - `0x00A7955B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A7954C  48 83 EC 28                     sub rsp, 0x28
00A79550  33 D2                           xor edx, edx
00A79552  44 8D 42 01                     lea r8d, [rdx + 1]
00A79556  E8 85 6A 9E FF                  call 0x14045ffe0
00A7955B  E8 50 43 7E FF                  call 0x14025d8b0
00A79560  48 83 C4 28                     add rsp, 0x28
00A79564  C3                              ret
00A79565  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DbgkpResumeProcess(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = PsThawMultiProcess(a1, a2, a2 + 1, a4);
    result = KeLeaveCriticalRegion(a1, a2, a2 + 1, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DbgkpResumeProcess(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = PsThawMultiProcess(Arg1, Arg2, Arg2 + 1, a4);
    result = KeLeaveCriticalRegion(Arg1, Arg2, Arg2 + 1, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A7954C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A7954C[BB_00A7954C]
  bb_00A79565[BB_00A79565]
```
