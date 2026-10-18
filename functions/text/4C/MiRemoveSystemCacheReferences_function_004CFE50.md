# MiRemoveSystemCacheReferences

- RVA: `0x004CFE50`–`0x004CFEEA` (길이 `154` bytes)
- VA: `0x00000001404CFE50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005E6B4`
- 디코드: `41`개 명령, `154/154` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004CFE8D` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x004CFEA0` → [MiRemoveViewsFromSection](../29/MiRemoveViewsFromSection_function_00298960.md) (function, `0x00298960`)
- `0x004CFEB4` → [MiCheckControlArea](../28/MiCheckControlArea_function_002861B0.md) (function, `0x002861B0`)
- `0x004CFEC9` → [MiReturnCrossPartitionSectionCharges](../4B/MiReturnCrossPartitionSectionCharges_function_004BA61C.md) (function, `0x004BA61C`)

### Direct callers
- [MmMapViewInSystemCache](../27/MmMapViewInSystemCache_function_00273094.md) at `0x00273318`

### Static image references
- `0x004CFE6F` → RVA `0x00E30088` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CFE50  48 8B C4                        mov rax, rsp
004CFE53  48 89 58 08                     mov qword ptr [rax + 8], rbx
004CFE57  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
004CFE5B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
004CFE5F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
004CFE63  41 56                           push r14
004CFE65  48 83 EC 20                     sub rsp, 0x20
004CFE69  48 8B 29                        mov rbp, qword ptr [rcx]
004CFE6C  48 8B F1                        mov rsi, rcx
004CFE6F  48 8B 05 12 02 96 00            mov rax, qword ptr [rip + 0x960212]
004CFE76  48 8B FA                        mov rdi, rdx
004CFE79  44 0F B7 45 3C                  movzx r8d, word ptr [rbp + 0x3c]
004CFE7E  48 8D 4D 48                     lea rcx, [rbp + 0x48]
004CFE82  41 81 E0 FF 03 00 00            and r8d, 0x3ff
004CFE89  4E 8B 34 C0                     mov r14, qword ptr [rax + r8*8]
004CFE8D  E8 FE 87 D7 FF                  call 0x140248690
004CFE92  41 B8 04 00 00 00               mov r8d, 4
004CFE98  48 8B D7                        mov rdx, rdi
004CFE9B  48 8B CE                        mov rcx, rsi
004CFE9E  8A D8                           mov bl, al
004CFEA0  E8 BB 8A DC FF                  call 0x140298960
004CFEA5  48 FF 4D 28                     dec qword ptr [rbp + 0x28]
004CFEA9  8A D3                           mov dl, bl
004CFEAB  FF 4D 58                        dec dword ptr [rbp + 0x58]
004CFEAE  48 8B CD                        mov rcx, rbp
004CFEB1  48 8B F8                        mov rdi, rax
004CFEB4  E8 F7 62 DB FF                  call 0x1402861b0
004CFEB9  48 85 FF                        test rdi, rdi
004CFEBC  74 10                           je 0x1404cfece
004CFEBE  4C 8B C7                        mov r8, rdi
004CFEC1  BA 01 00 00 00                  mov edx, 1
004CFEC6  49 8B CE                        mov rcx, r14
004CFEC9  E8 4E A7 FE FF                  call 0x1404ba61c
004CFECE  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004CFED3  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
004CFED8  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
004CFEDD  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
004CFEE2  48 83 C4 20                     add rsp, 0x20
004CFEE6  41 5E                           pop r14
004CFEE8  C3                              ret
004CFEE9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiRemoveSystemCacheReferences(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (32);
    a3 = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1) + 60)) & (0x3FFULL));
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(a1) + 72, a2, a3, a4);
    result = MiRemoveViewsFromSection(a1, a2, 4, a4);
    result = MiCheckControlArea(*(unsigned __int64 *)(a1), (unsigned __int8)((unsigned __int8)(result)), 4, a4);
    if (result != 0) {
        a3 = result;
        a2 = 1;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9830930) + a3 * 8);
        result = MiReturnCrossPartitionSectionCharges(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiRemoveSystemCacheReferences(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (32);
    a3 = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1) + 0x3C)) & (0x3FFULL));
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(arg1) + 72, Arg2, a3, a4);
    result = MiRemoveViewsFromSection(Arg1, Arg2, 4, a4);
    result = MiCheckControlArea(*(uint64_t *)(arg1), (uint8_t)((uint8_t)(result)), 4, a4);
    if (result != 0) {
        a3 = result;
        Arg2 = 1;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x960212) + a3 * 8);
        result = MiReturnCrossPartitionSectionCharges(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CFE50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004CFE50[BB_004CFE50]
  bb_004CFEBE[BB_004CFEBE]
  bb_004CFECE[BB_004CFECE]
  bb_004CFEE9[BB_004CFEE9]
  bb_004CFE50 -->|branch| bb_004CFECE
  bb_004CFE50 -->|fallthrough| bb_004CFEBE
  bb_004CFEBE -->|flow| bb_004CFECE
```
