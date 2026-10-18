# EtwpApcPoolDpc

- RVA: `0x004A2700`–`0x004A27BA` (길이 `186` bytes)
- VA: `0x00000001404A2700`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B5F04`
- 디코드: `47`개 명령, `186/186` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004A2750` → [EtwpQueueApc](../20/EtwpQueueApc_function_00203B7C.md) (function, `0x00203B7C`)
- `0x004A2771` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004A2790` → [ExReleaseRundownProtectionCacheAwareEx](../25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A2700  4C 8B DC                        mov r11, rsp
004A2703  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
004A2707  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
004A270B  49 89 7B 18                     mov qword ptr [r11 + 0x18], rdi
004A270F  4D 89 73 20                     mov qword ptr [r11 + 0x20], r14
004A2713  41 57                           push r15
004A2715  48 83 EC 40                     sub rsp, 0x40
004A2719  49 8B 38                        mov rdi, qword ptr [r8]
004A271C  49 8D 70 40                     lea rsi, [r8 + 0x40]
004A2720  48 8B 06                        mov rax, qword ptr [rsi]
004A2723  49 8B D8                        mov rbx, r8
004A2726  4D 8B 48 48                     mov r9, qword ptr [r8 + 0x48]
004A272A  48 8B CB                        mov rcx, rbx
004A272D  49 89 43 F0                     mov qword ptr [r11 - 0x10], rax
004A2731  49 8B 40 38                     mov rax, qword ptr [r8 + 0x38]
004A2735  48 8B 53 58                     mov rdx, qword ptr [rbx + 0x58]
004A2739  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
004A273D  49 8B 40 30                     mov rax, qword ptr [r8 + 0x30]
004A2741  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
004A2745  49 8B 40 50                     mov rax, qword ptr [r8 + 0x50]
004A2749  41 B0 02                        mov r8b, 2
004A274C  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
004A2750  E8 27 14 D6 FF                  call 0x140203b7c
004A2755  85 C0                           test eax, eax
004A2757  79 1D                           jns 0x1404a2776
004A2759  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
004A275D  4C 8D 4B 38                     lea r9, [rbx + 0x38]
004A2761  48 8B 53 58                     mov rdx, qword ptr [rbx + 0x58]
004A2765  4C 8D 43 30                     lea r8, [rbx + 0x30]
004A2769  48 8B CB                        mov rcx, rbx
004A276C  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
004A2771  E8 5A 83 21 00                  call 0x1406baad0
004A2776  48 8B 87 50 05 00 00            mov rax, qword ptr [rdi + 0x550]
004A277D  BA 01 00 00 00                  mov edx, 1
004A2782  44 8B 07                        mov r8d, dword ptr [rdi]
004A2785  48 8B 88 C0 02 00 00            mov rcx, qword ptr [rax + 0x2c0]
004A278C  4A 8B 0C C1                     mov rcx, qword ptr [rcx + r8*8]
004A2790  E8 BB C8 DB FF                  call 0x14025f050
004A2795  F0 0F BA B3 A0 00 00 00 01      lock btr dword ptr [rbx + 0xa0], 1
004A279E  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
004A27A3  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
004A27A8  48 8B 7C 24 60                  mov rdi, qword ptr [rsp + 0x60]
004A27AD  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
004A27B2  48 83 C4 40                     add rsp, 0x40
004A27B6  41 5F                           pop r15
004A27B8  C3                              ret
004A27B9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpApcPoolDpc(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 16) = *(unsigned __int64 *)(a3 + 64);
    *(unsigned __int64 *)(v_rsp - 24) = *(unsigned __int64 *)(a3 + 56);
    *(unsigned __int64 *)(v_rsp - 32) = *(unsigned __int64 *)(a3 + 48);
    *(unsigned __int64 *)(v_rsp - 40) = *(unsigned __int64 *)(a3 + 80);
    result = EtwpQueueApc(a3, *(unsigned __int64 *)(a3 + 88), 2, *(unsigned __int64 *)(a3 + 72));
    if (sign_flag) {
        result = *(unsigned __int64 *)(a3 + 80);
        a4 = a3 + 56;
        a2 = *(unsigned __int64 *)(a3 + 88);
        a3 = a3 + 48;
        a1 = a3;
        v_stack_m28 = a3 + 64;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    result = ExReleaseRundownProtectionCacheAwareEx(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 1360) + 704) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3))) * 8), 1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3))), a4);
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpApcPoolDpc(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x10) = *(uint64_t *)(arg3 + 0x40);
    *(uint64_t *)(local_rsp - 0x18) = *(uint64_t *)(arg3 + 0x38);
    *(uint64_t *)(local_rsp - 0x20) = *(uint64_t *)(arg3 + 0x30);
    *(uint64_t *)(local_rsp - 0x28) = *(uint64_t *)(arg3 + 0x50);
    result = EtwpQueueApc(Arg3, *(uint64_t *)(arg3 + 0x58), 2, *(uint64_t *)(arg3 + 0x48));
    if (sign_flag) {
        result = *(uint64_t *)(arg3 + 0x50);
        a4 = Arg3 + 56;
        Arg2 = *(uint64_t *)(arg3 + 0x58);
        Arg3 = Arg3 + 48;
        Arg1 = Arg3;
        v_stack_m28 = Arg3 + 64;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
    result = ExReleaseRundownProtectionCacheAwareEx(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg3) + 0x550) + 0x2C0) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3))) * 8), 1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg3))), a4);
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x30` | `64` | `R` |
| `Arg3` | `+ 0x38` | `64` | `R` |
| `Arg3` | `+ 0x40` | `64` | `R` |
| `Arg3` | `+ 0x48` | `64` | `R` |
| `Arg3` | `+ 0x50` | `64` | `R` |
| `Arg3` | `+ 0x58` | `64` | `R` |
| `Arg3` | `+ 0xA0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A2700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A2700[BB_004A2700]
  bb_004A2759[BB_004A2759]
  bb_004A2776[BB_004A2776]
  bb_004A27B9[BB_004A27B9]
  bb_004A2700 -->|branch| bb_004A2776
  bb_004A2700 -->|fallthrough| bb_004A2759
  bb_004A2759 -->|flow| bb_004A2776
```
