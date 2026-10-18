# SepInitSingletonEntry

- RVA: `0x002EEF64`–`0x002EEFA5` (길이 `65` bytes)
- VA: `0x00000001402EEF64`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `20`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002EEF71` → [SepGetSingletonEntryFromIndexNumber](../2F/SepGetSingletonEntryFromIndexNumber_function_002F095C.md) (function, `0x002F095C`)
- `0x002EEF81` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x002EEF94` → [ExReleaseSpinLockExclusive](../2C/ExReleaseSpinLockExclusive_function_002C0EF0.md) (function, `0x002C0EF0`)

### Direct callers
- [SepAddLuidToIndexEntry](../../page/A4/SepAddLuidToIndexEntry_function_00A425C0.md) at `0x00A426EB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002EEF64  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002EEF69  57                              push rdi
002EEF6A  48 83 EC 20                     sub rsp, 0x20
002EEF6E  48 8B FA                        mov rdi, rdx
002EEF71  E8 E6 19 00 00                  call 0x1402f095c
002EEF76  48 8B D8                        mov rbx, rax
002EEF79  48 85 C0                        test rax, rax
002EEF7C  74 1B                           je 0x1402eef99
002EEF7E  48 8B C8                        mov rcx, rax
002EEF81  E8 0A 97 F5 FF                  call 0x140248690
002EEF86  48 83 63 10 00                  and qword ptr [rbx + 0x10], 0
002EEF8B  8A D0                           mov dl, al
002EEF8D  48 8B CB                        mov rcx, rbx
002EEF90  48 89 7B 08                     mov qword ptr [rbx + 8], rdi
002EEF94  E8 57 1F FD FF                  call 0x1402c0ef0
002EEF99  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002EEF9E  48 83 C4 20                     add rsp, 0x20
002EEFA2  5F                              pop rdi
002EEFA3  C3                              ret
002EEFA4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepInitSingletonEntry(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = SepGetSingletonEntryFromIndexNumber(a1, a2, a3, a4);
    if (result != 0) {
        a1 = result;
        result = ExAcquireSpinLockExclusive(a1, a2, a3, a4);
        a2 = (unsigned __int8)(result);
        a1 = result;
        *(unsigned __int64 *)(result + 8) = a2;
        result = ExReleaseSpinLockExclusive(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepInitSingletonEntry(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = SepGetSingletonEntryFromIndexNumber(Arg1, Arg2, a3, a4);
    if (result != 0) {
        Arg1 = result;
        result = ExAcquireSpinLockExclusive(Arg1, Arg2, a3, a4);
        Arg2 = (uint8_t)(result);
        Arg1 = result;
        *(uint64_t *)(result + 0x8) = Arg2;
        result = ExReleaseSpinLockExclusive(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002EEF64&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002EEF64[BB_002EEF64]
  bb_002EEF7E[BB_002EEF7E]
  bb_002EEF99[BB_002EEF99]
  bb_002EEFA4[BB_002EEFA4]
  bb_002EEF64 -->|branch| bb_002EEF99
  bb_002EEF64 -->|fallthrough| bb_002EEF7E
  bb_002EEF7E -->|flow| bb_002EEF99
```
