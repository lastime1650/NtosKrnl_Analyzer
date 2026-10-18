# NtModifyDriverEntry

- RVA: `0x007CDCB0`–`0x007CDCD7` (길이 `39` bytes)
- VA: `0x00000001407CDCB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007CDCCC` → [ExpSetDriverEntry](ExpSetDriverEntry_function_007CC424.md) (function, `0x007CC424`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007CDCB4` → RVA `0x00EFF050` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007CDCB0  48 83 EC 28                     sub rsp, 0x28
007CDCB4  83 3D 95 13 73 00 02            cmp dword ptr [rip + 0x731395], 2
007CDCBB  74 07                           je 0x1407cdcc4
007CDCBD  B8 02 00 00 C0                  mov eax, 0xc0000002
007CDCC2  EB 0D                           jmp 0x1407cdcd1
007CDCC4  48 8B D1                        mov rdx, rcx
007CDCC7  45 33 C0                        xor r8d, r8d
007CDCCA  33 C9                           xor ecx, ecx
007CDCCC  E8 53 E7 FF FF                  call 0x1407cc424
007CDCD1  48 83 C4 28                     add rsp, 0x28
007CDCD5  C3                              ret
007CDCD6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtModifyDriverEntry(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(v_rip + 7541653)) == 2) goto loc_007CDCC4;
    goto loc_007CDCD1;
loc_007CDCC4:
    a3 = 0;
    a1 = 0;
    result = ExpSetDriverEntry(a1, a1, a3, a4);
loc_007CDCD1:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtModifyDriverEntry(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(v_rip + 0x731395)) == 2) goto loc_007CDCC4;
    goto loc_007CDCD1;
loc_007CDCC4:
    Arg3 = 0;
    Arg1 = 0;
    result = ExpSetDriverEntry(Arg1, Arg1, Arg3, a4);
loc_007CDCD1:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007CDCB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007CDCB0[BB_007CDCB0]
  bb_007CDCBD[BB_007CDCBD]
  bb_007CDCC4[BB_007CDCC4]
  bb_007CDCD1[BB_007CDCD1]
  bb_007CDCD6[BB_007CDCD6]
  bb_007CDCB0 -->|branch| bb_007CDCC4
  bb_007CDCB0 -->|fallthrough| bb_007CDCBD
  bb_007CDCBD -->|branch| bb_007CDCD1
  bb_007CDCC4 -->|flow| bb_007CDCD1
```
