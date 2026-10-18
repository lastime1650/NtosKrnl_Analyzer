# MiAllocateSlabEntry

- RVA: `0x004AE468`–`0x004AE4EB` (길이 `131` bytes)
- VA: `0x00000001404AE468`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A2790`
- 디코드: `35`개 명령, `131/131` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004AE4AC` → [MiAllocatePool](../35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x004AE4E1` → [KcsanMarkAddressIgnored](KcsanMarkAddressIgnored_function_004AE500.md) (function, `0x004AE500`)

### Direct callers
- [MiCreateSlabEntry](../37/MiCreateSlabEntry_function_00374DEC.md) at `0x00375025`
- [MiCreateBootSlabEntries](../../init/C6/MiCreateBootSlabEntries_function_00C69A50.md) at `0x00C69AB4`

### Static image references
- `0x004AE482` → RVA `0x00011C60` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004AE468  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004AE46D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
004AE472  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
004AE477  57                              push rdi
004AE478  48 83 EC 20                     sub rsp, 0x20
004AE47C  8B 81 88 00 00 00               mov eax, dword ptr [rcx + 0x88]
004AE482  48 8D 2D D7 37 B6 FF            lea rbp, [rip - 0x49c829]
004AE489  48 C1 E8 04                     shr rax, 4
004AE48D  48 8B F1                        mov rsi, rcx
004AE490  83 E0 03                        and eax, 3
004AE493  B9 40 00 00 00                  mov ecx, 0x40
004AE498  41 B8 4D 69 53 65               mov r8d, 0x6553694d
004AE49E  8B 6C C5 00                     mov ebp, dword ptr [rbp + rax*8]
004AE4A2  8B FD                           mov edi, ebp
004AE4A4  48 C1 EF 03                     shr rdi, 3
004AE4A8  48 8D 57 60                     lea rdx, [rdi + 0x60]
004AE4AC  E8 8F D0 EA FF                  call 0x14035b540
004AE4B1  48 8B D8                        mov rbx, rax
004AE4B4  48 85 C0                        test rax, rax
004AE4B7  75 16                           jne 0x1404ae4cf
004AE4B9  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004AE4BE  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
004AE4C3  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
004AE4C8  48 83 C4 20                     add rsp, 0x20
004AE4CC  5F                              pop rdi
004AE4CD  C3                              ret
004AE4CE  CC                              int3
004AE4CF  48 89 70 38                     mov qword ptr [rax + 0x38], rsi
004AE4D3  48 8D 48 60                     lea rcx, [rax + 0x60]
004AE4D7  48 8B D7                        mov rdx, rdi
004AE4DA  48 89 48 48                     mov qword ptr [rax + 0x48], rcx
004AE4DE  89 68 40                        mov dword ptr [rax + 0x40], ebp
004AE4E1  E8 1A 00 00 00                  call 0x1404ae500
004AE4E6  48 8B C3                        mov rax, rbx
004AE4E9  EB CE                           jmp 0x1404ae4b9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateSlabEntry(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = ((unsigned int)(*(unsigned int *)(a1 + 136))) >> (4);
    result = (unsigned int)((result) & (3));
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 4835369 + result * 8))))) >> (3);
    result = MiAllocatePool(64, v_rdi + 96, (unsigned int)(0x6553694DULL), a4);
    if (result != 0) goto loc_004AE4CF;
loc_004AE4B9:
    v_rsp = (v_rsp) + (32);
    return result;
loc_004AE4CF:
    *(unsigned __int64 *)(result + 56) = v_stack_p18;
    *(unsigned __int64 *)(result + 72) = result + 96;
    *(unsigned int *)(result + 64) = (unsigned int)(v_stack_p10);
    result = KcsanMarkAddressIgnored(result + 96, v_rdi, (unsigned int)(0x6553694DULL), a4);
    goto loc_004AE4B9;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateSlabEntry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x88))) >> (4);
    result = (uint32_t)((result) & (3));
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x49C829 + result * 8))))) >> (3);
    result = MiAllocatePool(64, local_rdi + 96, (uint32_t)(0x6553694DULL), a4);
    if (result != 0) goto loc_004AE4CF;
loc_004AE4B9:
    local_rsp = (local_rsp) + (32);
    return result;
loc_004AE4CF:
    *(uint64_t *)(result + 0x38) = v_stack_p18;
    *(uint64_t *)(result + 0x48) = result + 96;
    *(uint32_t *)(result + 0x40) = (uint32_t)(v_stack_p10);
    result = KcsanMarkAddressIgnored(result + 96, local_rdi, (uint32_t)(0x6553694DULL), a4);
    goto loc_004AE4B9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x88` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004AE468&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004AE468[BB_004AE468]
  bb_004AE4B9[BB_004AE4B9]
  bb_004AE4CE[BB_004AE4CE]
  bb_004AE4CF[BB_004AE4CF]
  bb_004AE468 -->|branch| bb_004AE4CF
  bb_004AE468 -->|fallthrough| bb_004AE4B9
  bb_004AE4CE -->|flow| bb_004AE4CF
  bb_004AE4CF -->|branch| bb_004AE4B9
```
