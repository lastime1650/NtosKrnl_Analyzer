# WmipUpdateRegistration

- RVA: `0x009E2BA4`–`0x009E2BE7` (길이 `67` bytes)
- VA: `0x00000001409E2BA4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF28`
- 디코드: `21`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009E2BAE` → [WmipFindRegEntryByDevice](../../text/46/WmipFindRegEntryByDevice_function_0046C22C.md) (function, `0x0046C22C`)
- `0x009E2BC3` → [WmipQueueRegWork](WmipQueueRegWork_function_009E2AC4.md) (function, `0x009E2AC4`)
- `0x009E2BCD` → [WmipUnreferenceRegEntry](../../text/47/WmipUnreferenceRegEntry_function_0047B6F0.md) (function, `0x0047B6F0`)

### Direct callers
- [IoWMIRegistrationControl](IoWMIRegistrationControl_function_009E2D60.md) at `0x009E2DE9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009E2BAE` → [WmipFindRegEntryByDevice](../../text/46/WmipFindRegEntryByDevice_function_0046C22C.md) (`PAGE` → `.text`)
  - `0x009E2BCD` → [WmipUnreferenceRegEntry](../../text/47/WmipUnreferenceRegEntry_function_0047B6F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009E2BA4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
009E2BA9  57                              push rdi
009E2BAA  48 83 EC 20                     sub rsp, 0x20
009E2BAE  E8 79 96 A8 FF                  call 0x14046c22c
009E2BB3  48 8B F8                        mov rdi, rax
009E2BB6  48 85 C0                        test rax, rax
009E2BB9  74 25                           je 0x1409e2be0
009E2BBB  48 8B D0                        mov rdx, rax
009E2BBE  B9 01 00 00 00                  mov ecx, 1
009E2BC3  E8 FC FE FF FF                  call 0x1409e2ac4
009E2BC8  48 8B CF                        mov rcx, rdi
009E2BCB  8B D8                           mov ebx, eax
009E2BCD  E8 1E 8B A9 FF                  call 0x14047b6f0
009E2BD2  8B C3                           mov eax, ebx
009E2BD4  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
009E2BD9  48 83 C4 20                     add rsp, 0x20
009E2BDD  5F                              pop rdi
009E2BDE  C3                              ret
009E2BDF  CC                              int3
009E2BE0  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009E2BE5  EB EB                           jmp 0x1409e2bd2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmipUpdateRegistration(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = WmipFindRegEntryByDevice(a1, a2, a3, a4);
    if (result == 0) goto loc_009E2BE0;
    result = WmipQueueRegWork(1, result, a3, a4);
    result = WmipUnreferenceRegEntry(result, result, a3, a4);
loc_009E2BD2:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_009E2BE0:
    goto loc_009E2BD2;
}
```

## 5. (Beta) C Style

```c
void WmipUpdateRegistration(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = WmipFindRegEntryByDevice(a1, a2, a3, a4);
    if (result == 0) goto loc_009E2BE0;
    result = WmipQueueRegWork(1, result, a3, a4);
    result = WmipUnreferenceRegEntry(result, result, a3, a4);
loc_009E2BD2:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_009E2BE0:
    goto loc_009E2BD2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009E2BA4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009E2BA4[BB_009E2BA4]
  bb_009E2BBB[BB_009E2BBB]
  bb_009E2BD2[BB_009E2BD2]
  bb_009E2BDF[BB_009E2BDF]
  bb_009E2BE0[BB_009E2BE0]
  bb_009E2BA4 -->|branch| bb_009E2BE0
  bb_009E2BA4 -->|fallthrough| bb_009E2BBB
  bb_009E2BBB -->|flow| bb_009E2BD2
  bb_009E2BDF -->|flow| bb_009E2BE0
  bb_009E2BE0 -->|branch| bb_009E2BD2
```
