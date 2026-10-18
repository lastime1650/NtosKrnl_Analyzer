# ViIsThreadInsidePagingCodePaths

- RVA: `0x00BAA2D4`–`0x00BAA337` (길이 `99` bytes)
- VA: `0x0000000140BAA2D4`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `29`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BAA2EE` → [ViRaiseIrqlToDpcLevel](../../text/61/ViRaiseIrqlToDpcLevel_function_006162B0.md) (function, `0x006162B0`)
- `0x00BAA2F8` → [ViDeadlockDetectionLock](ViDeadlockDetectionLock_function_00BA91C4.md) (function, `0x00BA91C4`)
- `0x00BAA300` → [ViDeadlockSearchThread](ViDeadlockSearchThread_function_00BAA1AC.md) (function, `0x00BAA1AC`)
- `0x00BAA317` → [ViDeadlockDetectionUnlock](ViDeadlockDetectionUnlock_function_00BA91FC.md) (function, `0x00BA91FC`)
- `0x00BAA31F` → [ViLowerIrql](../../text/61/ViLowerIrql_function_00616278.md) (function, `0x00616278`)

### Direct callers
- [VfDeadlockReleaseResource](../BB/VfDeadlockReleaseResource_function_00BB759C.md) at `0x00BB75FF`
- [VfDeadlockAcquireResource](../BB/VfDeadlockAcquireResource_function_00BB83B4.md) at `0x00BB845C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00BAA2EE` → [ViRaiseIrqlToDpcLevel](../../text/61/ViRaiseIrqlToDpcLevel_function_006162B0.md) (`PAGEVRFY` → `.text`)
  - `0x00BAA31F` → [ViLowerIrql](../../text/61/ViLowerIrql_function_00616278.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAA2D4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00BAA2D9  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00BAA2DE  57                              push rdi
00BAA2DF  48 83 EC 20                     sub rsp, 0x20
00BAA2E3  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
00BAA2EC  33 FF                           xor edi, edi
00BAA2EE  E8 BD BF A6 FF                  call 0x1406162b0
00BAA2F3  33 C9                           xor ecx, ecx
00BAA2F5  40 8A F0                        mov sil, al
00BAA2F8  E8 C7 EE FF FF                  call 0x140ba91c4
00BAA2FD  48 8B CB                        mov rcx, rbx
00BAA300  E8 A7 FE FF FF                  call 0x140baa1ac
00BAA305  48 85 C0                        test rax, rax
00BAA308  74 0B                           je 0x140baa315
00BAA30A  8B 48 2C                        mov ecx, dword ptr [rax + 0x2c]
00BAA30D  85 C9                           test ecx, ecx
00BAA30F  8D 47 01                        lea eax, [rdi + 1]
00BAA312  0F 45 F8                        cmovne edi, eax
00BAA315  33 C9                           xor ecx, ecx
00BAA317  E8 E0 EE FF FF                  call 0x140ba91fc
00BAA31C  40 8A CE                        mov cl, sil
00BAA31F  E8 54 BF A6 FF                  call 0x140616278
00BAA324  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00BAA329  8B C7                           mov eax, edi
00BAA32B  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00BAA330  48 83 C4 20                     add rsp, 0x20
00BAA334  5F                              pop rdi
00BAA335  C3                              ret
00BAA336  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViIsThreadInsidePagingCodePaths(int a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
    result = ViRaiseIrqlToDpcLevel(a1, a2, a3, a4);
    a1 = 0;
    result = ViDeadlockDetectionLock(a1, a2, a3, a4);
    result = ViDeadlockSearchThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    if (result != 0) {
        a1 = *(unsigned int *)(result + 44);
        result = v_rdi + 1;
        if (a1 != 0) { v_rdi = (unsigned int)(result); }
    }
    a1 = 0;
    result = ViDeadlockDetectionUnlock(a1, a2, a3, a4);
    result = ViLowerIrql((unsigned __int8)((unsigned __int8)(result)), a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rdi));
}
```

## 5. (Beta) C Style

```c
int64_t ViIsThreadInsidePagingCodePaths(int32_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    result = ViRaiseIrqlToDpcLevel(Arg1, a2, a3, a4);
    Arg1 = 0;
    result = ViDeadlockDetectionLock(Arg1, a2, a3, a4);
    result = ViDeadlockSearchThread(*(uint64_t *)(gs_base + (0 + 0x188)), a2, a3, a4);
    if (result != 0) {
        Arg1 = *(uint32_t *)(result + 0x2C);
        result = local_rdi + 1;
        if (Arg1 != 0) { local_rdi = (uint32_t)(result); }
    }
    Arg1 = 0;
    result = ViDeadlockDetectionUnlock(Arg1, a2, a3, a4);
    result = ViLowerIrql((uint8_t)((uint8_t)(result)), a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rdi));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAA2D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAA2D4[BB_00BAA2D4]
  bb_00BAA30A[BB_00BAA30A]
  bb_00BAA315[BB_00BAA315]
  bb_00BAA336[BB_00BAA336]
  bb_00BAA2D4 -->|branch| bb_00BAA315
  bb_00BAA2D4 -->|fallthrough| bb_00BAA30A
  bb_00BAA30A -->|flow| bb_00BAA315
```
