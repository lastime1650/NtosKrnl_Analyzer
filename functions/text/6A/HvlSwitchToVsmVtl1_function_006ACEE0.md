# HvlSwitchToVsmVtl1

- RVA: `0x006ACEE0`–`0x006AD01B` (길이 `315` bytes)
- VA: `0x00000001406ACEE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFDF0`
- 디코드: `62`개 명령, `315/315` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006ACF86` → [HvlpSwitchToVsmVtl1RetpolineHelper](HvlpSwitchToVsmVtl1RetpolineHelper_function_006AD030.md) (function, `0x006AD030`)

### Direct callers
- [sub_00235EB4](../23/Unknown_function_00235EB4.md) at `0x00235F9F`
- [sub_002361D4](../23/Unknown_function_002361D4.md) at `0x002361F4`
- [sub_002361D4](../23/Unknown_function_002361D4.md) at `0x00236238`
- [sub_002361D4](../23/Unknown_function_002361D4.md) at `0x002362A9`

### Static image references
- `0x006ACF7F` → RVA `0x01201860` (`CFGRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006ACEE0  48 81 EC 38 01 00 00            sub rsp, 0x138
006ACEE7  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
006ACEEF  0F 29 74 24 30                  movaps xmmword ptr [rsp + 0x30], xmm6
006ACEF4  0F 29 7C 24 40                  movaps xmmword ptr [rsp + 0x40], xmm7
006ACEF9  44 0F 29 44 24 50               movaps xmmword ptr [rsp + 0x50], xmm8
006ACEFF  44 0F 29 4C 24 60               movaps xmmword ptr [rsp + 0x60], xmm9
006ACF05  44 0F 29 54 24 70               movaps xmmword ptr [rsp + 0x70], xmm10
006ACF0B  44 0F 29 58 80                  movaps xmmword ptr [rax - 0x80], xmm11
006ACF10  44 0F 29 60 90                  movaps xmmword ptr [rax - 0x70], xmm12
006ACF15  44 0F 29 68 A0                  movaps xmmword ptr [rax - 0x60], xmm13
006ACF1A  44 0F 29 70 B0                  movaps xmmword ptr [rax - 0x50], xmm14
006ACF1F  44 0F 29 78 C0                  movaps xmmword ptr [rax - 0x40], xmm15
006ACF24  48 89 68 F8                     mov qword ptr [rax - 8], rbp
006ACF28  48 89 18                        mov qword ptr [rax], rbx
006ACF2B  48 89 78 08                     mov qword ptr [rax + 8], rdi
006ACF2F  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
006ACF33  4C 89 60 18                     mov qword ptr [rax + 0x18], r12
006ACF37  4C 89 68 20                     mov qword ptr [rax + 0x20], r13
006ACF3B  4C 89 70 28                     mov qword ptr [rax + 0x28], r14
006ACF3F  4C 89 78 30                     mov qword ptr [rax + 0x30], r15
006ACF43  48 89 54 24 08                  mov qword ptr [rsp + 8], rdx
006ACF48  48 8B 1A                        mov rbx, qword ptr [rdx]
006ACF4B  F3 44 0F 6F 52 08               movdqu xmm10, xmmword ptr [rdx + 8]
006ACF51  F3 44 0F 6F 5A 18               movdqu xmm11, xmmword ptr [rdx + 0x18]
006ACF57  F3 44 0F 6F 62 28               movdqu xmm12, xmmword ptr [rdx + 0x28]
006ACF5D  F3 44 0F 6F 6A 38               movdqu xmm13, xmmword ptr [rdx + 0x38]
006ACF63  F3 44 0F 6F 72 48               movdqu xmm14, xmmword ptr [rdx + 0x48]
006ACF69  F3 44 0F 6F 7A 58               movdqu xmm15, xmmword ptr [rdx + 0x58]
006ACF6F  4D 8B C8                        mov r9, r8
006ACF72  45 0F 20 C0                     mov r8, cr8
006ACF76  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
006ACF7F  48 8B 05 DA 48 B5 00            mov rax, qword ptr [rip + 0xb548da]
006ACF86  E8 A5 00 00 00                  call 0x1406ad030
006ACF8B  48 8B 54 24 08                  mov rdx, qword ptr [rsp + 8]
006ACF90  48 89 1A                        mov qword ptr [rdx], rbx
006ACF93  F3 44 0F 7F 52 08               movdqu xmmword ptr [rdx + 8], xmm10
006ACF99  F3 44 0F 7F 5A 18               movdqu xmmword ptr [rdx + 0x18], xmm11
006ACF9F  F3 44 0F 7F 62 28               movdqu xmmword ptr [rdx + 0x28], xmm12
006ACFA5  F3 44 0F 7F 6A 38               movdqu xmmword ptr [rdx + 0x38], xmm13
006ACFAB  F3 44 0F 7F 72 48               movdqu xmmword ptr [rdx + 0x48], xmm14
006ACFB1  F3 44 0F 7F 7A 58               movdqu xmmword ptr [rdx + 0x58], xmm15
006ACFB7  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
006ACFBF  0F 28 74 24 30                  movaps xmm6, xmmword ptr [rsp + 0x30]
006ACFC4  0F 28 7C 24 40                  movaps xmm7, xmmword ptr [rsp + 0x40]
006ACFC9  44 0F 28 44 24 50               movaps xmm8, xmmword ptr [rsp + 0x50]
006ACFCF  44 0F 28 4C 24 60               movaps xmm9, xmmword ptr [rsp + 0x60]
006ACFD5  44 0F 28 54 24 70               movaps xmm10, xmmword ptr [rsp + 0x70]
006ACFDB  44 0F 28 59 80                  movaps xmm11, xmmword ptr [rcx - 0x80]
006ACFE0  44 0F 28 61 90                  movaps xmm12, xmmword ptr [rcx - 0x70]
006ACFE5  44 0F 28 69 A0                  movaps xmm13, xmmword ptr [rcx - 0x60]
006ACFEA  44 0F 28 71 B0                  movaps xmm14, xmmword ptr [rcx - 0x50]
006ACFEF  44 0F 28 79 C0                  movaps xmm15, xmmword ptr [rcx - 0x40]
006ACFF4  48 8B 19                        mov rbx, qword ptr [rcx]
006ACFF7  48 8B 79 08                     mov rdi, qword ptr [rcx + 8]
006ACFFB  48 8B 71 10                     mov rsi, qword ptr [rcx + 0x10]
006ACFFF  4C 8B 61 18                     mov r12, qword ptr [rcx + 0x18]
006AD003  4C 8B 69 20                     mov r13, qword ptr [rcx + 0x20]
006AD007  4C 8B 71 28                     mov r14, qword ptr [rcx + 0x28]
006AD00B  4C 8B 79 30                     mov r15, qword ptr [rcx + 0x30]
006AD00F  48 8B 69 F8                     mov rbp, qword ptr [rcx - 8]
006AD013  48 81 C4 38 01 00 00            add rsp, 0x138
006AD01A  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlSwitchToVsmVtl1(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (312);
    v_stack_m108 = v_xmm6;
    v_stack_mF8 = v_xmm7;
    v_stack_mE8 = v_xmm8;
    v_stack_mD8 = v_xmm9;
    v_stack_mC8 = v_xmm10;
    *(unsigned __int64 *)(v_stack_m38 - 128) = v_xmm11;
    *(unsigned __int64 *)(v_stack_m38 - 112) = v_xmm12;
    *(unsigned __int64 *)(v_stack_m38 - 96) = v_xmm13;
    *(unsigned __int64 *)(v_stack_m38 - 80) = v_xmm14;
    *(unsigned __int64 *)(v_stack_m38 - 64) = v_xmm15;
    *(unsigned __int64 *)(v_stack_m38 - 8) = v_rbp;
    *(unsigned __int64 *)(v_stack_m38) = v_rbx;
    *(unsigned __int64 *)(v_stack_m38 + 8) = v_rdi;
    *(unsigned __int64 *)(v_stack_m38 + 16) = v_rsi;
    *(unsigned __int64 *)(v_stack_m38 + 24) = v_r12;
    *(unsigned __int64 *)(v_stack_m38 + 32) = v_r13;
    *(unsigned __int64 *)(v_stack_m38 + 40) = v_r14;
    *(unsigned __int64 *)(v_stack_m38 + 48) = v_r15;
    v_stack_m130 = a2;
    result = HvlpSwitchToVsmVtl1RetpolineHelper(a1, a2, v_cr8, a3);
    *(unsigned __int64 *)(v_stack_m130) = *(unsigned __int64 *)(a2);
    *(unsigned __int64 *)(v_stack_m130 + 8) = v_xmm10;
    *(unsigned __int64 *)(v_stack_m130 + 24) = v_xmm11;
    *(unsigned __int64 *)(v_stack_m130 + 40) = v_xmm12;
    *(unsigned __int64 *)(v_stack_m130 + 56) = v_xmm13;
    *(unsigned __int64 *)(v_stack_m130 + 72) = v_xmm14;
    *(unsigned __int64 *)(v_stack_m130 + 88) = v_xmm15;
    v_rsp = (v_rsp) + (312);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlSwitchToVsmVtl1(int64_t Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint64_t v_stack_m130;
    uint64_t v_stack_m38;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (312);
    v_stack_m108 = v_xmm6;
    v_stack_mF8 = v_xmm7;
    v_stack_mE8 = v_xmm8;
    v_stack_mD8 = v_xmm9;
    v_stack_mC8 = v_xmm10;
    *(uint64_t *)(v_stack_m38 - 0x80) = v_xmm11;
    *(uint64_t *)(v_stack_m38 - 0x70) = v_xmm12;
    *(uint64_t *)(v_stack_m38 - 0x60) = v_xmm13;
    *(uint64_t *)(v_stack_m38 - 0x50) = v_xmm14;
    *(uint64_t *)(v_stack_m38 - 0x40) = v_xmm15;
    *(uint64_t *)(v_stack_m38 - 0x8) = local_rbp;
    *(uint64_t *)(v_stack_m38) = local_rbx;
    *(uint64_t *)(v_stack_m38 + 0x8) = local_rdi;
    *(uint64_t *)(v_stack_m38 + 0x10) = local_rsi;
    *(uint64_t *)(v_stack_m38 + 0x18) = local_r12;
    *(uint64_t *)(v_stack_m38 + 0x20) = local_r13;
    *(uint64_t *)(v_stack_m38 + 0x28) = local_r14;
    *(uint64_t *)(v_stack_m38 + 0x30) = local_r15;
    v_stack_m130 = Arg2;
    result = HvlpSwitchToVsmVtl1RetpolineHelper(Arg1, Arg2, v_cr8, Arg3);
    *(uint64_t *)(v_stack_m130) = *(uint64_t *)(arg2);
    *(uint64_t *)(v_stack_m130 + 0x8) = v_xmm10;
    *(uint64_t *)(v_stack_m130 + 0x18) = v_xmm11;
    *(uint64_t *)(v_stack_m130 + 0x28) = v_xmm12;
    *(uint64_t *)(v_stack_m130 + 0x38) = v_xmm13;
    *(uint64_t *)(v_stack_m130 + 0x48) = v_xmm14;
    *(uint64_t *)(v_stack_m130 + 0x58) = v_xmm15;
    local_rsp = (local_rsp) + (312);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `128` | `R` |
| `Arg2` | `+ 0x18` | `128` | `R` |
| `Arg2` | `+ 0x28` | `128` | `R` |
| `Arg2` | `+ 0x38` | `128` | `R` |
| `Arg2` | `+ 0x48` | `128` | `R` |
| `Arg2` | `+ 0x58` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ACEE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006ACEE0[BB_006ACEE0]
```
