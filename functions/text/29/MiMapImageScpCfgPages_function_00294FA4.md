# MiMapImageScpCfgPages

- RVA: `0x00294FA4`–`0x002950F5` (길이 `337` bytes)
- VA: `0x0000000140294FA4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067800`
- 디코드: `78`개 명령, `337/337` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00295016` → [PsGetScpCfgPageTypeForProcess](../../page/A4/PsGetScpCfgPageTypeForProcess_function_00A42258.md) (function, `0x00A42258`)
- `0x00295045` → [MiIncrementCombinedPte](../22/MiIncrementCombinedPte_function_0022B248.md) (function, `0x0022B248`)
- `0x00295059` → [MiLockVad](MiLockVad_function_00295810.md) (function, `0x00295810`)
- `0x00295062` → [MiMakePrototypePteDirect](MiMakePrototypePteDirect_function_00294DE0.md) (function, `0x00294DE0`)
- `0x00295077` → [MiGetImageExtensionBaseAddress](../../page/A3/MiGetImageExtensionBaseAddress_function_00A3559C.md) (function, `0x00A3559C`)
- `0x002950CC` → [MiDecommitPages](../24/MiDecommitPages_function_00241BD0.md) (function, `0x00241BD0`)
- `0x002950D7` → [MiUnlockVad](../2A/MiUnlockVad_function_002A59C8.md) (function, `0x002A59C8`)

### Direct callers
- [MiMapAllImageScpPages](../../page/8D/MiMapAllImageScpPages_function_008D0534.md) at `0x008D05CB`
- [MiMapViewOfImageSection](../../page/97/MiMapViewOfImageSection_function_0097E92C.md) at `0x0097F465`

### Static image references
- `0x00295024` → RVA `0x00E2D8A0` (`.data`; read)
- `0x0029502A` → RVA `0x00E2D8B8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00295016` → [PsGetScpCfgPageTypeForProcess](../../page/A4/PsGetScpCfgPageTypeForProcess_function_00A42258.md) (`.text` → `PAGE`)
  - `0x00295077` → [MiGetImageExtensionBaseAddress](../../page/A3/MiGetImageExtensionBaseAddress_function_00A3559C.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00294FA4  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00294FA9  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00294FAE  56                              push rsi
00294FAF  57                              push rdi
00294FB0  41 56                           push r14
00294FB2  48 81 EC 80 00 00 00            sub rsp, 0x80
00294FB9  33 C0                           xor eax, eax
00294FBB  0F 57 C0                        xorps xmm0, xmm0
00294FBE  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00294FC3  4C 8B F2                        mov r14, rdx
00294FC6  48 8B 81 10 04 00 00            mov rax, qword ptr [rcx + 0x410]
00294FCD  48 8B E9                        mov rbp, rcx
00294FD0  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00294FD5  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
00294FDA  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
00294FDF  F6 80 25 04 00 00 04            test byte ptr [rax + 0x425], 4
00294FE6  0F 84 F0 00 00 00               je 0x1402950dc
00294FEC  48 8B 42 48                     mov rax, qword ptr [rdx + 0x48]
00294FF0  48 8B 08                        mov rcx, qword ptr [rax]
00294FF3  48 8B 41 60                     mov rax, qword ptr [rcx + 0x60]
00294FF7  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00294FFB  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00294FFF  48 8D 51 48                     lea rdx, [rcx + 0x48]
00295003  48 F7 D9                        neg rcx
00295006  48 8B CD                        mov rcx, rbp
00295009  48 1B C0                        sbb rax, rax
0029500C  48 23 C2                        and rax, rdx
0029500F  44 8A 00                        mov r8b, byte ptr [rax]
00295012  41 80 E0 01                     and r8b, 1
00295016  E8 3D D2 7A 00                  call 0x140a42258
0029501B  83 F8 04                        cmp eax, 4
0029501E  0F 84 B8 00 00 00               je 0x1402950dc
00295024  8B 3D 76 88 B9 00               mov edi, dword ptr [rip + 0xb98876]
0029502A  48 8D 0D 87 88 B9 00            lea rcx, [rip + 0xb98887]
00295031  48 98                           cdqe
00295033  45 33 C0                        xor r8d, r8d
00295036  48 8B 1C C1                     mov rbx, qword ptr [rcx + rax*8]
0029503A  48 8D 8D 00 04 00 00            lea rcx, [rbp + 0x400]
00295041  48 8D 53 20                     lea rdx, [rbx + 0x20]
00295045  E8 FE 61 F9 FF                  call 0x14022b248
0029504A  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
00295053  49 8B D6                        mov rdx, r14
00295056  48 8B CE                        mov rcx, rsi
00295059  E8 B2 07 00 00                  call 0x140295810
0029505E  48 8D 4B 20                     lea rcx, [rbx + 0x20]
00295062  E8 79 FD FF FF                  call 0x140294de0
00295067  48 0F BA E8 0B                  bts rax, 0xb
0029506C  49 8B CE                        mov rcx, r14
0029506F  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
00295077  E8 20 05 7A 00                  call 0x140a3559c
0029507C  48 8D 0C 07                     lea rcx, [rdi + rax]
00295080  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
0029508A  48 C1 E9 09                     shr rcx, 9
0029508E  48 23 C8                        and rcx, rax
00295091  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
0029509B  48 03 C8                        add rcx, rax
0029509E  45 33 C0                        xor r8d, r8d
002950A1  48 8D 44 24 40                  lea rax, [rsp + 0x40]
002950A6  4C 8B CD                        mov r9, rbp
002950A9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
002950AE  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
002950B6  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
002950BB  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
002950C3  41 8D 50 01                     lea edx, [r8 + 1]
002950C7  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
002950CC  E8 FF CA FA FF                  call 0x140241bd0
002950D1  49 8B D6                        mov rdx, r14
002950D4  48 8B CE                        mov rcx, rsi
002950D7  E8 EC 08 01 00                  call 0x1402a59c8
002950DC  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
002950E4  49 8B 5B 28                     mov rbx, qword ptr [r11 + 0x28]
002950E8  49 8B 6B 30                     mov rbp, qword ptr [r11 + 0x30]
002950EC  49 8B E3                        mov rsp, r11
002950EF  41 5E                           pop r14
002950F1  5F                              pop rdi
002950F2  5E                              pop rsi
002950F3  C3                              ret
002950F4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMapImageScpCfgPages(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_rsp = (v_rsp) - (128);
    result = 0;
    v_stack_m28 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 1040) + 1061)) & (4)) == 0) goto loc_002950DC;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 72)) + 96)) & (-8);
    a1 = -(*(unsigned __int64 *)(result + 32));
    result = (result) & (*(unsigned __int64 *)(result + 32) + 72);
    a3 = (unsigned __int8)((*(unsigned __int8 *)(result)) & (1));
    result = PsGetScpCfgPageTypeForProcess(a1, *(unsigned __int64 *)(result + 32) + 72, a3, a4);
    if (((unsigned int)(result)) != 4) {
        v_rdi = *(unsigned int *)(v_rip + 12159094);
        a1 = v_rip + 12159111;
        a3 = 0;
        v_rbx = *(unsigned __int64 *)(a1 + result * 8);
        a1 = a1 + 1024;
        a2 = v_rbx + 32;
        result = MiIncrementCombinedPte(a1, a2, a3, a4);
        v_rsi = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = a2;
        a1 = v_rsi;
        result = MiLockVad(a1, a2, a3, a4);
        a1 = v_rbx + 32;
        result = MiMakePrototypePteDirect(a1, a2, a3, a4);
        a1 = a2;
        v_stack_p8 = result;
        result = MiGetImageExtensionBaseAddress(a1, a2, a3, a4);
        a1 = v_rdi + result * 1;
        a1 = (a1) >> (9);
        a1 = (a1) & (result);
        a1 = (a1) + (result);
        a3 = 0;
        result = v_stack_m58;
        a4 = a1;
        v_stack_m60 = result;
        result = v_stack_p8;
        v_stack_m68 = result;
        v_stack_m70 = 1;
        a2 = a3 + 1;
        v_stack_m78 = a2;
        result = MiDecommitPages(a1, a2, a3, a4);
        a2 = a2;
        a1 = v_rsi;
        result = MiUnlockVad(a1, a2, a3, a4);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiMapImageScpCfgPages(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    local_rsp = (local_rsp) - (128);
    result = 0;
    v_stack_m28 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x410) + 0x425)) & (4)) == 0) goto loc_002950DC;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x48)) + 0x60)) & (-8);
    Arg1 = -(*(uint64_t *)(result + 0x20));
    result = (result) & (*(uint64_t *)(result + 0x20) + 72);
    a3 = (uint8_t)((*(uint8_t *)(result)) & (1));
    result = PsGetScpCfgPageTypeForProcess(Arg1, *(uint64_t *)(result + 0x20) + 72, a3, a4);
    if (((uint32_t)(result)) != 4) {
        local_rdi = *(uint32_t *)(v_rip + 0xB98876);
        Arg1 = v_rip + 12159111;
        a3 = 0;
        local_rbx = *(uint64_t *)(arg1 + result * 8);
        Arg1 = Arg1 + 1024;
        Arg2 = local_rbx + 32;
        result = MiIncrementCombinedPte(Arg1, Arg2, a3, a4);
        local_rsi = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = Arg2;
        Arg1 = local_rsi;
        result = MiLockVad(Arg1, Arg2, a3, a4);
        Arg1 = local_rbx + 32;
        result = MiMakePrototypePteDirect(Arg1, Arg2, a3, a4);
        Arg1 = Arg2;
        v_stack_p8 = result;
        result = MiGetImageExtensionBaseAddress(Arg1, Arg2, a3, a4);
        Arg1 = local_rdi + result * 1;
        Arg1 = (Arg1) >> (9);
        Arg1 = (Arg1) & (result);
        Arg1 = (Arg1) + (result);
        a3 = 0;
        result = v_stack_m58;
        a4 = Arg1;
        v_stack_m60 = result;
        result = v_stack_p8;
        v_stack_m68 = result;
        v_stack_m70 = 1;
        Arg2 = a3 + 1;
        v_stack_m78 = Arg2;
        result = MiDecommitPages(Arg1, Arg2, a3, a4);
        Arg2 = Arg2;
        Arg1 = local_rsi;
        result = MiUnlockVad(Arg1, Arg2, a3, a4);
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x400` | `64` | `R` |
| `Arg1` | `+ 0x410` | `64` | `R` |
| `Arg2` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00294FA4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00294FA4[BB_00294FA4]
  bb_00294FEC[BB_00294FEC]
  bb_00295024[BB_00295024]
  bb_002950DC[BB_002950DC]
  bb_002950F4[BB_002950F4]
  bb_00294FA4 -->|branch| bb_002950DC
  bb_00294FA4 -->|fallthrough| bb_00294FEC
  bb_00294FEC -->|branch| bb_002950DC
  bb_00294FEC -->|fallthrough| bb_00295024
  bb_00295024 -->|flow| bb_002950DC
```
