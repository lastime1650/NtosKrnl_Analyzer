# flush_pending

- RVA: `0x005F5258`–`0x005F52CD` (길이 `117` bytes)
- VA: `0x00000001405F5258`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005C954`
- 디코드: `35`개 명령, `117/117` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005F5276` → [bi_flush](../60/bi_flush_function_00600ED0.md) (function, `0x00600ED0`)
- `0x005F5297` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [deflate](deflate_function_005F35C8.md) at `0x005F3619`
- [deflate](deflate_function_005F35C8.md) at `0x005F377B`
- [deflate](deflate_function_005F35C8.md) at `0x005F3832`
- [deflate](deflate_function_005F35C8.md) at `0x005F38AA`
- [deflate_fast](deflate_fast_function_005F3A80.md) at `0x005F3EE6`
- [deflate_fast](deflate_fast_function_005F3A80.md) at `0x005F3F64`
- [deflate_fast](deflate_fast_function_005F3A80.md) at `0x005F3FBA`
- [deflate_huff](deflate_huff_function_005F3FDC.md) at `0x005F40CA`
- [deflate_huff](deflate_huff_function_005F3FDC.md) at `0x005F412E`
- [deflate_rle](deflate_rle_function_005F414C.md) at `0x005F43AD`
- [deflate_rle](deflate_rle_function_005F414C.md) at `0x005F440E`
- [deflate_slow](deflate_slow_function_005F4430.md) at `0x005F4840`
- [deflate_slow](deflate_slow_function_005F4430.md) at `0x005F48FC`
- [deflate_slow](deflate_slow_function_005F4430.md) at `0x005F4A02`
- [deflate_slow](deflate_slow_function_005F4430.md) at `0x005F4A54`
- [deflate_stored](deflate_stored_function_005F4A80.md) at `0x005F4BA2`
- [deflate_stored](deflate_stored_function_005F4A80.md) at `0x005F4EBE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005F5258  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005F525D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
005F5262  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
005F5267  57                              push rdi
005F5268  48 83 EC 20                     sub rsp, 0x20
005F526C  48 8B 79 28                     mov rdi, qword ptr [rcx + 0x28]
005F5270  48 8B F1                        mov rsi, rcx
005F5273  48 8B CF                        mov rcx, rdi
005F5276  E8 55 BC 00 00                  call 0x140600ed0
005F527B  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
005F527E  8B 6E 18                        mov ebp, dword ptr [rsi + 0x18]
005F5281  3B C5                           cmp eax, ebp
005F5283  0F 46 E8                        cmovbe ebp, eax
005F5286  85 ED                           test ebp, ebp
005F5288  74 2D                           je 0x1405f52b7
005F528A  48 8B 57 20                     mov rdx, qword ptr [rdi + 0x20]
005F528E  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
005F5292  44 8B C5                        mov r8d, ebp
005F5295  8B DD                           mov ebx, ebp
005F5297  E8 A4 15 0D 00                  call 0x1406c6840
005F529C  48 01 5E 10                     add qword ptr [rsi + 0x10], rbx
005F52A0  48 01 5F 20                     add qword ptr [rdi + 0x20], rbx
005F52A4  01 6E 1C                        add dword ptr [rsi + 0x1c], ebp
005F52A7  29 6E 18                        sub dword ptr [rsi + 0x18], ebp
005F52AA  29 6F 28                        sub dword ptr [rdi + 0x28], ebp
005F52AD  75 08                           jne 0x1405f52b7
005F52AF  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
005F52B3  48 89 47 20                     mov qword ptr [rdi + 0x20], rax
005F52B7  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005F52BC  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
005F52C1  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
005F52C6  48 83 C4 20                     add rsp, 0x20
005F52CA  5F                              pop rdi
005F52CB  C3                              ret
005F52CC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall flush_pending(__int64 a1)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = bi_flush(*(unsigned __int64 *)(a1 + 40), a2, a3, a4);
    v_rbp = (unsigned int)(*(unsigned int *)(a1 + 24));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 40)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24))))) { v_rbp = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 40) + 40))); }
    if ((unsigned int)(v_rbp) == 0) goto loc_005F52B7;
    result = memcpy(*(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 32), (unsigned int)((unsigned int)(v_rbp)), a4);
    if ((unsigned int)(v_rbp) == 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 16);
        *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 40) + 32) = result;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t flush_pending(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = bi_flush(*(uint64_t *)(arg1 + 0x28), a2, a3, a4);
    local_rbp = (uint32_t)(*(uint32_t *)(arg1 + 0x18));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x28)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18))))) { local_rbp = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x28) + 0x28))); }
    if ((uint32_t)(local_rbp) == 0) goto loc_005F52B7;
    result = memcpy(*(uint64_t *)(arg1 + 0x10), *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x20), (uint32_t)((uint32_t)(local_rbp)), a4);
    if ((uint32_t)(local_rbp) == 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x10);
        *(uint64_t *)(*(uint64_t *)(arg1 + 0x28) + 0x20) = result;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R/W` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R/W` |
| `Arg1` | `+ 0x1C` | `32` | `R/W` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005F5258&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005F5258[BB_005F5258]
  bb_005F528A[BB_005F528A]
  bb_005F52AF[BB_005F52AF]
  bb_005F52B7[BB_005F52B7]
  bb_005F52CC[BB_005F52CC]
  bb_005F5258 -->|branch| bb_005F52B7
  bb_005F5258 -->|fallthrough| bb_005F528A
  bb_005F528A -->|branch| bb_005F52B7
  bb_005F528A -->|fallthrough| bb_005F52AF
  bb_005F52AF -->|flow| bb_005F52B7
```
