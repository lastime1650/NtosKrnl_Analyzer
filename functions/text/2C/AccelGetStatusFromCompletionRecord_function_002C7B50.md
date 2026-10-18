# AccelGetStatusFromCompletionRecord

- RVA: `0x002C7B50`–`0x002C7BC3` (길이 `115` bytes)
- VA: `0x00000001402C7B50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EE3C`
- 디코드: `30`개 명령, `115/115` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002C7B6D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002C7BAD` → [AccelpInternalOperationHandler](AccelpInternalOperationHandler_function_002C7DAC.md) (function, `0x002C7DAC`)

### Direct callers
- [AccelpSubmitWork](AccelpSubmitWork_function_002C8190.md) at `0x002C81D3`
- [SmHwAcceleratorWaitForRequest](../61/SmHwAcceleratorWaitForRequest_function_00611A7C.md) at `0x00611ADF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C7B50  40 53                           push rbx
002C7B52  48 81 EC 90 00 00 00            sub rsp, 0x90
002C7B59  33 C0                           xor eax, eax
002C7B5B  48 8B D9                        mov rbx, rcx
002C7B5E  33 D2                           xor edx, edx
002C7B60  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
002C7B64  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
002C7B69  44 8D 40 6C                     lea r8d, [rax + 0x6c]
002C7B6D  E8 CE F0 3F 00                  call 0x1406c6c40
002C7B72  48 85 DB                        test rbx, rbx
002C7B75  74 45                           je 0x1402c7bbc
002C7B77  48 8B 03                        mov rax, qword ptr [rbx]
002C7B7A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
002C7B7F  48 83 64 24 48 00               and qword ptr [rsp + 0x48], 0
002C7B85  33 D2                           xor edx, edx
002C7B87  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
002C7B8C  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
002C7B8F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002C7B93  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
002C7B97  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002C7B9C  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
002C7BA0  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002C7BA5  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
002C7BAD  E8 FA 01 00 00                  call 0x1402c7dac
002C7BB2  48 81 C4 90 00 00 00            add rsp, 0x90
002C7BB9  5B                              pop rbx
002C7BBA  C3                              ret
002C7BBB  CC                              int3
002C7BBC  B8 0D 00 00 C0                  mov eax, 0xc000000d
002C7BC1  EB EF                           jmp 0x1402c7bb2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AccelGetStatusFromCompletionRecord(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;

    v_rsp = (v_rsp) - (144);
    result = 0;
    a2 = 0;
    v_stack_m74 = 0;
    result = memset(v_stack_m78, a2, result + 108, a4);
    if (a1 == 0) goto loc_002C7BBC;
    a2 = 0;
    v_stack_m70 = *(unsigned __int64 *)(a1);
    v_stack_m68 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    v_stack_m60 = *(unsigned __int64 *)(a1 + 24);
    v_stack_m58 = *(unsigned __int64 *)(a1 + 32);
    v_stack_m78 = 3;
    result = AccelpInternalOperationHandler(v_stack_m78, a2, result + 108, a4);
loc_002C7BB2:
    v_rsp = (v_rsp) + (144);
    return result;
loc_002C7BBC:
    goto loc_002C7BB2;
}
```

## 5. (Beta) C Style

```c
int64_t AccelGetStatusFromCompletionRecord(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;

    local_rsp = (local_rsp) - (144);
    result = 0;
    Arg2 = 0;
    v_stack_m74 = 0;
    result = memset(v_stack_m78, Arg2, result + 108, a4);
    if (Arg1 == 0) goto loc_002C7BBC;
    Arg2 = 0;
    v_stack_m70 = *(uint64_t *)(Arg1);
    v_stack_m68 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)));
    v_stack_m60 = *(uint64_t *)(Arg1 + 0x18);
    v_stack_m58 = *(uint64_t *)(Arg1 + 0x20);
    v_stack_m78 = 3;
    result = AccelpInternalOperationHandler(v_stack_m78, Arg2, result + 108, a4);
loc_002C7BB2:
    local_rsp = (local_rsp) + (144);
    return result;
loc_002C7BBC:
    goto loc_002C7BB2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C7B50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C7B50[BB_002C7B50]
  bb_002C7B77[BB_002C7B77]
  bb_002C7BB2[BB_002C7BB2]
  bb_002C7BBB[BB_002C7BBB]
  bb_002C7BBC[BB_002C7BBC]
  bb_002C7B50 -->|branch| bb_002C7BBC
  bb_002C7B50 -->|fallthrough| bb_002C7B77
  bb_002C7B77 -->|flow| bb_002C7BB2
  bb_002C7BBB -->|flow| bb_002C7BBC
  bb_002C7BBC -->|branch| bb_002C7BB2
```
