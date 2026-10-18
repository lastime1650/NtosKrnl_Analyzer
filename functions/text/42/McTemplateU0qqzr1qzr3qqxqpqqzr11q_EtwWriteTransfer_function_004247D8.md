# McTemplateU0qqzr1qzr3qqxqpqqzr11q_EtwWriteTransfer

- RVA: `0x004247D8`–`0x0042494F` (길이 `375` bytes)
- VA: `0x00000001404247D8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A0408`
- 디코드: `74`개 명령, `375/375` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00424934` → [McGenEventWrite_EtwWriteTransfer](McGenEventWrite_EtwWriteTransfer_function_00424FC8.md) (function, `0x00424FC8`)
- `0x00424940` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [Pdcv2EventWrite_ACTIVATION_CLIENT_DEACTIVATE](Pdcv2EventWrite_ACTIVATION_CLIENT_DEACTIVATE_function_00424588.md) at `0x004246AA`

### Static image references
- `0x004247EF` → RVA `0x00E0A740` (`.data`; read)
- `0x00424814` → RVA `0x00E08870` (`.data`; read)
- `0x0042484A` → RVA `0x00013F80` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004247D8  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
004247DD  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
004247E2  55                              push rbp
004247E3  48 8D 6C 24 C0                  lea rbp, [rsp - 0x40]
004247E8  48 81 EC 40 01 00 00            sub rsp, 0x140
004247EF  48 8B 05 4A 5F 9E 00            mov rax, qword ptr [rip + 0x9e5f4a]
004247F6  48 33 C4                        xor rax, rsp
004247F9  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
004247FD  33 D2                           xor edx, edx
004247FF  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
00424807  48 8D 45 60                     lea rax, [rbp + 0x60]
0042480B  89 54 24 7C                     mov dword ptr [rsp + 0x7c], edx
0042480F  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00424814  48 8D 0D 55 40 9E 00            lea rcx, [rip + 0x9e4055]
0042481B  48 8D 45 68                     lea rax, [rbp + 0x68]
0042481F  89 55 9C                        mov dword ptr [rbp - 0x64], edx
00424822  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00424827  45 33 C0                        xor r8d, r8d
0042482A  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
0042482E  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00424833  43 8D 04 09                     lea eax, [r9 + r9]
00424837  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
0042483B  44 8D 4A 0F                     lea r9d, [rdx + 0xf]
0042483F  48 8D 45 78                     lea rax, [rbp + 0x78]
00424843  89 55 1C                        mov dword ptr [rbp + 0x1c], edx
00424846  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0042484A  48 8D 15 2F F7 BE FF            lea rdx, [rip - 0x4108d1]
00424851  48 8B 85 80 00 00 00            mov rax, qword ptr [rbp + 0x80]
00424858  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0042485C  8B 45 78                        mov eax, dword ptr [rbp + 0x78]
0042485F  03 C0                           add eax, eax
00424861  48 C7 44 24 58 04 00 00 00      mov qword ptr [rsp + 0x58], 4
0042486A  89 45 98                        mov dword ptr [rbp - 0x68], eax
0042486D  48 8D 85 88 00 00 00            lea rax, [rbp + 0x88]
00424874  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00424878  48 8D 85 90 00 00 00            lea rax, [rbp + 0x90]
0042487F  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00424883  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
0042488A  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0042488E  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
00424895  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00424899  48 8D 85 A8 00 00 00            lea rax, [rbp + 0xa8]
004248A0  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
004248A4  48 8D 44 24 30                  lea rax, [rsp + 0x30]
004248A9  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
004248AD  48 8D 85 B8 00 00 00            lea rax, [rbp + 0xb8]
004248B4  48 89 45 00                     mov qword ptr [rbp], rax
004248B8  48 8B 85 C0 00 00 00            mov rax, qword ptr [rbp + 0xc0]
004248BF  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
004248C3  8B 85 B8 00 00 00               mov eax, dword ptr [rbp + 0xb8]
004248C9  03 C0                           add eax, eax
004248CB  48 C7 44 24 68 04 00 00 00      mov qword ptr [rsp + 0x68], 4
004248D4  89 45 18                        mov dword ptr [rbp + 0x18], eax
004248D7  48 8D 85 C8 00 00 00            lea rax, [rbp + 0xc8]
004248DE  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
004248E2  48 8D 44 24 40                  lea rax, [rsp + 0x40]
004248E7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004248EC  48 C7 45 88 04 00 00 00         mov qword ptr [rbp - 0x78], 4
004248F4  48 C7 45 A8 04 00 00 00         mov qword ptr [rbp - 0x58], 4
004248FC  48 C7 45 B8 04 00 00 00         mov qword ptr [rbp - 0x48], 4
00424904  48 C7 45 C8 08 00 00 00         mov qword ptr [rbp - 0x38], 8
0042490C  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
00424914  48 C7 45 E8 08 00 00 00         mov qword ptr [rbp - 0x18], 8
0042491C  48 C7 45 F8 04 00 00 00         mov qword ptr [rbp - 8], 4
00424924  48 C7 45 08 04 00 00 00         mov qword ptr [rbp + 8], 4
0042492C  48 C7 45 28 04 00 00 00         mov qword ptr [rbp + 0x28], 4
00424934  E8 8F 06 00 00                  call 0x140424fc8
00424939  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0042493D  48 33 CC                        xor rcx, rsp
00424940  E8 FB 7C 28 00                  call 0x1406ac640
00424945  48 81 C4 40 01 00 00            add rsp, 0x140
0042494C  5D                              pop rbp
0042494D  C3                              ret
0042494E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall McTemplateU0qqzr1qzr3qqxqpqqzr11q_EtwWriteTransfer(__int64 a1, int a2, int a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, unsigned int a14, __int64 a15, __int64 a16)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;

    v_stack_p20 = (unsigned int)(a4);
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 10379082)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    v_stack_m118 = 2;
    v_stack_mCC = 0;
    v_stack_mF8 = v_stack_p18;
    v_stack_mAC = 0;
    v_stack_mE8 = v_stack_p20;
    a3 = 0;
    v_stack_mD8 = a5;
    v_stack_mD0 = (unsigned int)(a4 + a4 * 1);
    v_stack_m2C = 0;
    v_stack_mC8 = a6;
    v_stack_mB8 = a7;
    result = (unsigned int)(((unsigned int)(a6)) + ((unsigned int)((unsigned int)(a6))));
    v_stack_mF0 = 4;
    v_stack_mB0 = (unsigned int)(result);
    v_stack_mA8 = a8;
    v_stack_m98 = a9;
    v_stack_m88 = a10;
    v_stack_m78 = a11;
    v_stack_m68 = a12;
    v_stack_m58 = v_stack_m118;
    v_stack_m48 = a14;
    v_stack_m38 = a15;
    result = (unsigned int)(((unsigned int)(a14)) + ((unsigned int)((unsigned int)(a14))));
    v_stack_mE0 = 4;
    v_stack_m30 = (unsigned int)(result);
    v_stack_m28 = a16;
    v_stack_m128 = v_stack_m108;
    v_stack_mC0 = 4;
    v_stack_mA0 = 4;
    v_stack_m90 = 4;
    v_stack_m80 = 8;
    v_stack_m70 = 4;
    v_stack_m60 = 8;
    v_stack_m50 = 4;
    v_stack_m40 = 4;
    v_stack_m20 = 4;
    result = McGenEventWrite_EtwWriteTransfer(v_rip + 10371157, v_rip - 4262097, a3, a2 + 15);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 4262097, a3, a2 + 15);
    v_rsp = (v_rsp) + (320);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t McTemplateU0qqzr1qzr3qqxqpqqzr11q_EtwWriteTransfer(int64_t Arg1, int32_t Arg2, int32_t Arg3, void *Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, uint64_t Arg13, uint32_t Arg14, int64_t Arg15, int64_t Arg16)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m108;
    uint32_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;

    v_stack_p20 = (uint32_t)(Arg4);
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0x9E5F4A)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    v_stack_m118 = 2;
    v_stack_mCC = 0;
    v_stack_mF8 = v_stack_p18;
    v_stack_mAC = 0;
    v_stack_mE8 = v_stack_p20;
    Arg3 = 0;
    v_stack_mD8 = Arg5;
    v_stack_mD0 = (uint32_t)(Arg4 + Arg4 * 1);
    v_stack_m2C = 0;
    v_stack_mC8 = Arg6;
    v_stack_mB8 = Arg7;
    result = (uint32_t)(((uint32_t)(Arg6)) + ((uint32_t)((uint32_t)(Arg6))));
    v_stack_mF0 = 4;
    v_stack_mB0 = (uint32_t)(result);
    v_stack_mA8 = Arg8;
    v_stack_m98 = Arg9;
    v_stack_m88 = Arg10;
    v_stack_m78 = Arg11;
    v_stack_m68 = Arg12;
    v_stack_m58 = v_stack_m118;
    v_stack_m48 = Arg14;
    v_stack_m38 = Arg15;
    result = (uint32_t)(((uint32_t)(Arg14)) + ((uint32_t)((uint32_t)(Arg14))));
    v_stack_mE0 = 4;
    v_stack_m30 = (uint32_t)(result);
    v_stack_m28 = Arg16;
    v_stack_m128 = v_stack_m108;
    v_stack_mC0 = 4;
    v_stack_mA0 = 4;
    v_stack_m90 = 4;
    v_stack_m80 = 8;
    v_stack_m70 = 4;
    v_stack_m60 = 8;
    v_stack_m50 = 4;
    v_stack_m40 = 4;
    v_stack_m20 = 4;
    result = McGenEventWrite_EtwWriteTransfer(v_rip + 10371157, v_rip - 4262097, Arg3, Arg2 + 15);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 4262097, Arg3, Arg2 + 15);
    local_rsp = (local_rsp) + (320);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0 + r9*1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004247D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004247D8[BB_004247D8]
  bb_0042494E[BB_0042494E]
```
