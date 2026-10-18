# CmpQueryKeyName

- RVA: `0x008A8960`–`0x008A8983` (길이 `35` bytes)
- VA: `0x00000001408A8960`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F31C`
- 디코드: `10`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008A896E` → [CmpDoQueryKeyName](../../text/45/CmpDoQueryKeyName_function_00456664.md) (function, `0x00456664`)

### Direct callers
- [ObQueryNameStringMode](ObQueryNameStringMode_function_008A7ED0.md) at `0x008A7FB9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008A896E` → [CmpDoQueryKeyName](../../text/45/CmpDoQueryKeyName_function_00456664.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008A8960  48 83 EC 48                     sub rsp, 0x48
008A8964  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008A8969  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008A896E  E8 F1 DC BA FF                  call 0x140456664
008A8973  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008A8977  EB 04                           jmp 0x1408a897d
008A8979  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008A897D  48 83 C4 48                     add rsp, 0x48
008A8981  C3                              ret
008A8982  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpQueryKeyName(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m28 = a5;
    result = CmpDoQueryKeyName(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    goto loc_008A897D;
loc_008A897D:
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpQueryKeyName(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m28 = Arg5;
    result = CmpDoQueryKeyName(Arg1, Arg2, Arg3, Arg4);
    v_stack_m18 = (uint32_t)(result);
    goto loc_008A897D;
loc_008A897D:
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A8960&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008A8960[BB_008A8960]
  bb_008A8979[BB_008A8979]
  bb_008A897D[BB_008A897D]
  bb_008A8982[BB_008A8982]
  bb_008A8960 -->|branch| bb_008A897D
  bb_008A8979 -->|flow| bb_008A897D
```
