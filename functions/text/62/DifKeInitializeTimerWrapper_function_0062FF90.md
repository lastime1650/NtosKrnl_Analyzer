# DifKeInitializeTimerWrapper

- RVA: `0x0062FF90`–`0x006300F6` (길이 `358` bytes)
- VA: `0x000000014062FF90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00084C9C`
- 디코드: `99`개 명령, `358/358` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062FFB7` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062FFE2` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00630010` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00630037` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00630050` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00630097` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006300BE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006300D7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062FFEC` → RVA `0x00F048B8` (`.data`; read)
- `0x0062FFFD` → RVA `0x00F04980` (`.data`; read)
- `0x00630009` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062FF90  48 8B C4                        mov rax, rsp
0062FF93  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062FF97  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062FF9B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062FF9F  57                              push rdi
0062FFA0  41 56                           push r14
0062FFA2  41 57                           push r15
0062FFA4  48 83 EC 30                     sub rsp, 0x30
0062FFA8  48 8B D9                        mov rbx, rcx
0062FFAB  0F 57 C0                        xorps xmm0, xmm0
0062FFAE  B9 17 01 00 00                  mov ecx, 0x117
0062FFB3  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062FFB7  E8 78 5A E6 FF                  call 0x140495a34
0062FFBC  45 33 FF                        xor r15d, r15d
0062FFBF  48 8B F0                        mov rsi, rax
0062FFC2  48 85 C0                        test rax, rax
0062FFC5  0F 84 8A 00 00 00               je 0x140630055
0062FFCB  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062FFCE  A8 18                           test al, 0x18
0062FFD0  74 0C                           je 0x14062ffde
0062FFD2  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062FFD7  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062FFDC  EB 0E                           jmp 0x14062ffec
0062FFDE  A8 04                           test al, 4
0062FFE0  74 0A                           je 0x14062ffec
0062FFE2  E8 21 3C EA FF                  call 0x1404d3c08
0062FFE7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062FFEC  44 38 3D C5 48 8D 00            cmp byte ptr [rip + 0x8d48c5], r15b
0062FFF3  41 8A EF                        mov bpl, r15b
0062FFF6  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0062FFFB  75 0C                           jne 0x140630009
0062FFFD  F7 05 79 49 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4979], 0x800
00630007  74 13                           je 0x14063001c
00630009  48 8D 0D 70 3E 8D 00            lea rcx, [rip + 0x8d3e70]
00630010  E8 0B 66 BE FF                  call 0x140216620
00630015  40 8A E8                        mov bpl, al
00630018  84 C0                           test al, al
0063001A  74 39                           je 0x140630055
0063001C  4C 8D 76 20                     lea r14, [rsi + 0x20]
00630020  49 8B 3E                        mov rdi, qword ptr [r14]
00630023  EB 1A                           jmp 0x14063003f
00630025  48 8D 47 F0                     lea rax, [rdi - 0x10]
00630029  48 85 C0                        test rax, rax
0063002C  74 0E                           je 0x14063003c
0063002E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00630032  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00630037  E8 94 AA 08 00                  call 0x1406baad0
0063003C  48 8B 3F                        mov rdi, qword ptr [rdi]
0063003F  49 3B FE                        cmp rdi, r14
00630042  75 E1                           jne 0x140630025
00630044  40 84 ED                        test bpl, bpl
00630047  74 0C                           je 0x140630055
00630049  48 8D 0D 30 3E 8D 00            lea rcx, [rip + 0x8d3e30]
00630050  E8 2B 9E D1 FF                  call 0x140349e80
00630055  4C 89 3B                        mov qword ptr [rbx], r15
00630058  48 8D 43 08                     lea rax, [rbx + 8]
0063005C  C6 03 08                        mov byte ptr [rbx], 8
0063005F  48 89 40 08                     mov qword ptr [rax + 8], rax
00630063  48 89 00                        mov qword ptr [rax], rax
00630066  4C 89 7B 18                     mov qword ptr [rbx + 0x18], r15
0063006A  44 89 7B 3C                     mov dword ptr [rbx + 0x3c], r15d
0063006E  66 44 89 7B 38                  mov word ptr [rbx + 0x38], r15w
00630073  48 85 F6                        test rsi, rsi
00630076  74 64                           je 0x1406300dc
00630078  44 38 3D 39 48 8D 00            cmp byte ptr [rip + 0x8d4839], r15b
0063007F  41 8A FF                        mov dil, r15b
00630082  75 0C                           jne 0x140630090
00630084  F7 05 F2 48 8D 00 00 08 00 00   test dword ptr [rip + 0x8d48f2], 0x800
0063008E  74 13                           je 0x1406300a3
00630090  48 8D 0D E9 3D 8D 00            lea rcx, [rip + 0x8d3de9]
00630097  E8 84 65 BE FF                  call 0x140216620
0063009C  40 8A F8                        mov dil, al
0063009F  84 C0                           test al, al
006300A1  74 39                           je 0x1406300dc
006300A3  48 83 C6 30                     add rsi, 0x30
006300A7  48 8B 1E                        mov rbx, qword ptr [rsi]
006300AA  EB 1A                           jmp 0x1406300c6
006300AC  48 8D 43 F0                     lea rax, [rbx - 0x10]
006300B0  48 85 C0                        test rax, rax
006300B3  74 0E                           je 0x1406300c3
006300B5  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006300B9  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006300BE  E8 0D AA 08 00                  call 0x1406baad0
006300C3  48 8B 1B                        mov rbx, qword ptr [rbx]
006300C6  48 3B DE                        cmp rbx, rsi
006300C9  75 E1                           jne 0x1406300ac
006300CB  40 84 FF                        test dil, dil
006300CE  74 0C                           je 0x1406300dc
006300D0  48 8D 0D A9 3D 8D 00            lea rcx, [rip + 0x8d3da9]
006300D7  E8 A4 9D D1 FF                  call 0x140349e80
006300DC  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
006300E1  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
006300E6  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006300EB  48 83 C4 30                     add rsp, 0x30
006300EF  41 5F                           pop r15
006300F1  41 5E                           pop r14
006300F3  5F                              pop rdi
006300F4  C3                              ret
006300F5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeInitializeTimerWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(279, a2, a3, a4);
    v_r15 = 0;
    if (result == 0) goto loc_00630055;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062FFDE;
    v_stack_m28 = v_stack_p0;
    goto loc_0062FFEC;
loc_0062FFDE:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9259205)) != 0) goto loc_00630009;
    if (((*(unsigned int *)(v_rip + 9259385)) & (0x800ULL)) == 0) goto loc_0063001C;
loc_00630009:
    result = ExAcquireRundownProtection(v_rip + 9256560, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00630055;
loc_0063001C:
    goto loc_0063003F;
loc_00630025:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063003F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00630025;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9256496;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(a1) = 0;
    *(unsigned __int8 *)(a1) = 8;
    *(unsigned __int64 *)(a1 + 8 + 8) = a1 + 8;
    *(unsigned __int64 *)(a1 + 8) = a1 + 8;
    *(unsigned __int64 *)(a1 + 24) = 0;
    *(unsigned int *)(a1 + 60) = 0;
    *(unsigned __int16 *)(a1 + 56) = 0;
    if (result == 0) goto loc_006300DC;
    if ((*(unsigned __int8 *)(v_rip + 9259065)) != 0) goto loc_00630090;
    if (((*(unsigned int *)(v_rip + 9259250)) & (0x800ULL)) == 0) goto loc_006300A3;
loc_00630090:
    result = ExAcquireRundownProtection(v_rip + 9256425, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006300DC;
loc_006300A3:
    v_rsi = (result) + (48);
    goto loc_006300C6;
loc_006300AC:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006300C6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006300AC;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9256361;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeInitializeTimerWrapper(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(279, a2, a3, a4);
    local_r15 = 0;
    if (result == 0) goto loc_00630055;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062FFDE;
    v_stack_m28 = v_stack_p0;
    goto loc_0062FFEC;
loc_0062FFDE:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D48C5)) != 0) goto loc_00630009;
    if (((*(uint32_t *)(v_rip + 0x8D4979)) & (0x800ULL)) == 0) goto loc_0063001C;
loc_00630009:
    result = ExAcquireRundownProtection(v_rip + 9256560, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00630055;
loc_0063001C:
    goto loc_0063003F;
loc_00630025:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063003F:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00630025;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9256496;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    *(uint64_t *)(arg1) = 0;
    *(uint8_t *)(arg1) = 8;
    *(void **)(arg1 + 0x8 + 0x8) = Arg1 + 8;
    *(void **)(arg1 + 0x8) = Arg1 + 8;
    *(uint64_t *)(arg1 + 0x18) = 0;
    *(uint32_t *)(arg1 + 0x3C) = 0;
    *(uint16_t *)(arg1 + 0x38) = 0;
    if (result == 0) goto loc_006300DC;
    if ((*(uint8_t *)(v_rip + 0x8D4839)) != 0) goto loc_00630090;
    if (((*(uint32_t *)(v_rip + 0x8D48F2)) & (0x800ULL)) == 0) goto loc_006300A3;
loc_00630090:
    result = ExAcquireRundownProtection(v_rip + 9256425, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006300DC;
loc_006300A3:
    local_rsi = (result) + (48);
    goto loc_006300C6;
loc_006300AC:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006300C6:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006300AC;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9256361;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x38` | `16` | `W` |
| `Arg1` | `+ 0x3C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062FF90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062FF90[BB_0062FF90]
  bb_0062FFCB[BB_0062FFCB]
  bb_0062FFD2[BB_0062FFD2]
  bb_0062FFDE[BB_0062FFDE]
  bb_0062FFE2[BB_0062FFE2]
  bb_0062FFEC[BB_0062FFEC]
  bb_0062FFFD[BB_0062FFFD]
  bb_00630009[BB_00630009]
  bb_0063001C[BB_0063001C]
  bb_00630025[BB_00630025]
  bb_0063002E[BB_0063002E]
  bb_0063003C[BB_0063003C]
  bb_0063003F[BB_0063003F]
  bb_00630044[BB_00630044]
  bb_00630049[BB_00630049]
  bb_00630055[BB_00630055]
  bb_00630078[BB_00630078]
  bb_00630084[BB_00630084]
  bb_00630090[BB_00630090]
  bb_006300A3[BB_006300A3]
  bb_006300AC[BB_006300AC]
  bb_006300B5[BB_006300B5]
  bb_006300C3[BB_006300C3]
  bb_006300C6[BB_006300C6]
  bb_006300CB[BB_006300CB]
  bb_006300D0[BB_006300D0]
  bb_006300DC[BB_006300DC]
  bb_006300F5[BB_006300F5]
  bb_0062FF90 -->|branch| bb_00630055
  bb_0062FF90 -->|fallthrough| bb_0062FFCB
  bb_0062FFCB -->|branch| bb_0062FFDE
  bb_0062FFCB -->|fallthrough| bb_0062FFD2
  bb_0062FFD2 -->|branch| bb_0062FFEC
  bb_0062FFDE -->|branch| bb_0062FFEC
  bb_0062FFDE -->|fallthrough| bb_0062FFE2
  bb_0062FFE2 -->|flow| bb_0062FFEC
  bb_0062FFEC -->|branch| bb_00630009
  bb_0062FFEC -->|fallthrough| bb_0062FFFD
  bb_0062FFFD -->|branch| bb_0063001C
  bb_0062FFFD -->|fallthrough| bb_00630009
  bb_00630009 -->|branch| bb_00630055
  bb_00630009 -->|fallthrough| bb_0063001C
  bb_0063001C -->|branch| bb_0063003F
  bb_00630025 -->|branch| bb_0063003C
  bb_00630025 -->|fallthrough| bb_0063002E
  bb_0063002E -->|flow| bb_0063003C
  bb_0063003C -->|flow| bb_0063003F
  bb_0063003F -->|branch| bb_00630025
  bb_0063003F -->|fallthrough| bb_00630044
  bb_00630044 -->|branch| bb_00630055
  bb_00630044 -->|fallthrough| bb_00630049
  bb_00630049 -->|flow| bb_00630055
  bb_00630055 -->|branch| bb_006300DC
  bb_00630055 -->|fallthrough| bb_00630078
  bb_00630078 -->|branch| bb_00630090
  bb_00630078 -->|fallthrough| bb_00630084
  bb_00630084 -->|branch| bb_006300A3
  bb_00630084 -->|fallthrough| bb_00630090
  bb_00630090 -->|branch| bb_006300DC
  bb_00630090 -->|fallthrough| bb_006300A3
  bb_006300A3 -->|branch| bb_006300C6
  bb_006300AC -->|branch| bb_006300C3
  bb_006300AC -->|fallthrough| bb_006300B5
  bb_006300B5 -->|flow| bb_006300C3
  bb_006300C3 -->|flow| bb_006300C6
  bb_006300C6 -->|branch| bb_006300AC
  bb_006300C6 -->|fallthrough| bb_006300CB
  bb_006300CB -->|branch| bb_006300DC
  bb_006300CB -->|fallthrough| bb_006300D0
  bb_006300D0 -->|flow| bb_006300DC
```
