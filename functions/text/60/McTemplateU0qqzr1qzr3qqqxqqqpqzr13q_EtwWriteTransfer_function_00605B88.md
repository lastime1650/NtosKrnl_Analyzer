# McTemplateU0qqzr1qzr3qqqxqqqpqzr13q_EtwWriteTransfer

- RVA: `0x00605B88`–`0x00605D2A` (길이 `418` bytes)
- VA: `0x0000000140605B88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D06D4`
- 디코드: `79`개 명령, `418/418` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00605D0F` → [McGenEventWrite_EtwWriteTransfer](../42/McGenEventWrite_EtwWriteTransfer_function_00424FC8.md) (function, `0x00424FC8`)
- `0x00605D1B` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [Pdcv2EventWrite_ACTIVATION_CLIENT_RENEW_ACTIVATION](Pdcv2EventWrite_ACTIVATION_CLIENT_RENEW_ACTIVATION_function_00606074.md) at `0x006061B2`

### Static image references
- `0x00605B9F` → RVA `0x00E0A740` (`.data`; read)
- `0x00605BC5` → RVA `0x00E08870` (`.data`; read)
- `0x00605C02` → RVA `0x000377B8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00605B88  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
00605B8D  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00605B92  55                              push rbp
00605B93  48 8D 6C 24 B0                  lea rbp, [rsp - 0x50]
00605B98  48 81 EC 50 01 00 00            sub rsp, 0x150
00605B9F  48 8B 05 9A 4B 80 00            mov rax, qword ptr [rip + 0x804b9a]
00605BA6  48 33 C4                        xor rax, rsp
00605BA9  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
00605BAD  33 D2                           xor edx, edx
00605BAF  48 C7 44 24 48 04 00 00 00      mov qword ptr [rsp + 0x48], 4
00605BB8  48 8D 45 70                     lea rax, [rbp + 0x70]
00605BBC  89 54 24 6C                     mov dword ptr [rsp + 0x6c], edx
00605BC0  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00605BC5  48 8D 0D A4 2C 80 00            lea rcx, [rip + 0x802ca4]
00605BCC  48 8D 45 78                     lea rax, [rbp + 0x78]
00605BD0  89 55 8C                        mov dword ptr [rbp - 0x74], edx
00605BD3  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00605BD8  45 33 C0                        xor r8d, r8d
00605BDB  48 8B 85 80 00 00 00            mov rax, qword ptr [rbp + 0x80]
00605BE2  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00605BE7  43 8D 04 09                     lea eax, [r9 + r9]
00605BEB  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00605BEF  44 8D 4A 11                     lea r9d, [rdx + 0x11]
00605BF3  48 8D 85 88 00 00 00            lea rax, [rbp + 0x88]
00605BFA  89 55 2C                        mov dword ptr [rbp + 0x2c], edx
00605BFD  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00605C02  48 8D 15 AF 1B A3 FF            lea rdx, [rip - 0x5ce451]
00605C09  48 8B 85 90 00 00 00            mov rax, qword ptr [rbp + 0x90]
00605C10  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00605C14  8B 85 88 00 00 00               mov eax, dword ptr [rbp + 0x88]
00605C1A  03 C0                           add eax, eax
00605C1C  48 C7 44 24 58 04 00 00 00      mov qword ptr [rsp + 0x58], 4
00605C25  89 45 88                        mov dword ptr [rbp - 0x78], eax
00605C28  48 8D 85 98 00 00 00            lea rax, [rbp + 0x98]
00605C2F  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00605C33  48 8D 85 A0 00 00 00            lea rax, [rbp + 0xa0]
00605C3A  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00605C3E  48 8D 85 A8 00 00 00            lea rax, [rbp + 0xa8]
00605C45  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00605C49  48 8D 85 B0 00 00 00            lea rax, [rbp + 0xb0]
00605C50  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00605C54  48 8D 85 B8 00 00 00            lea rax, [rbp + 0xb8]
00605C5B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00605C5F  48 8D 85 C0 00 00 00            lea rax, [rbp + 0xc0]
00605C66  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00605C6A  48 8D 85 C8 00 00 00            lea rax, [rbp + 0xc8]
00605C71  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00605C75  48 8D 85 D0 00 00 00            lea rax, [rbp + 0xd0]
00605C7C  48 89 45 00                     mov qword ptr [rbp], rax
00605C80  48 8D 85 D8 00 00 00            lea rax, [rbp + 0xd8]
00605C87  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00605C8B  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
00605C92  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00605C96  8B 85 D8 00 00 00               mov eax, dword ptr [rbp + 0xd8]
00605C9C  03 C0                           add eax, eax
00605C9E  48 C7 44 24 78 04 00 00 00      mov qword ptr [rsp + 0x78], 4
00605CA7  89 45 28                        mov dword ptr [rbp + 0x28], eax
00605CAA  48 8D 85 E8 00 00 00            lea rax, [rbp + 0xe8]
00605CB1  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
00605CB5  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00605CBA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00605CBF  48 C7 45 98 04 00 00 00         mov qword ptr [rbp - 0x68], 4
00605CC7  48 C7 45 A8 04 00 00 00         mov qword ptr [rbp - 0x58], 4
00605CCF  48 C7 45 B8 04 00 00 00         mov qword ptr [rbp - 0x48], 4
00605CD7  48 C7 45 C8 08 00 00 00         mov qword ptr [rbp - 0x38], 8
00605CDF  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
00605CE7  48 C7 45 E8 04 00 00 00         mov qword ptr [rbp - 0x18], 4
00605CEF  48 C7 45 F8 04 00 00 00         mov qword ptr [rbp - 8], 4
00605CF7  48 C7 45 08 08 00 00 00         mov qword ptr [rbp + 8], 8
00605CFF  48 C7 45 18 04 00 00 00         mov qword ptr [rbp + 0x18], 4
00605D07  48 C7 45 38 04 00 00 00         mov qword ptr [rbp + 0x38], 4
00605D0F  E8 B4 F2 E1 FF                  call 0x140424fc8
00605D14  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00605D18  48 33 CC                        xor rcx, rsp
00605D1B  E8 20 69 0A 00                  call 0x1406ac640
00605D20  48 81 C4 50 01 00 00            add rsp, 0x150
00605D27  5D                              pop rbp
00605D28  C3                              ret
00605D29  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall McTemplateU0qqzr1qzr3qqqxqqqpqzr13q_EtwWriteTransfer(__int64 a1, int a2, int a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, unsigned int a16, __int64 a17, __int64 a18)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m138;
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
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;

    v_stack_p20 = (unsigned int)(a4);
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (336);
    result = (*(unsigned __int64 *)(v_rip + 8407962)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    v_stack_m110 = 4;
    v_stack_mEC = 0;
    v_stack_m118 = v_stack_p18;
    v_stack_mCC = 0;
    v_stack_m108 = v_stack_p20;
    a3 = 0;
    v_stack_mF8 = a5;
    v_stack_mF0 = (unsigned int)(a4 + a4 * 1);
    v_stack_m2C = 0;
    v_stack_mE8 = a6;
    v_stack_mD8 = a7;
    result = (unsigned int)(((unsigned int)(a6)) + ((unsigned int)((unsigned int)(a6))));
    v_stack_m100 = 4;
    v_stack_mD0 = (unsigned int)(result);
    v_stack_mC8 = a8;
    v_stack_mB8 = a9;
    v_stack_mA8 = a10;
    v_stack_m98 = a11;
    v_stack_m88 = a12;
    v_stack_m78 = a13;
    v_stack_m68 = a14;
    v_stack_m58 = a15;
    v_stack_m48 = a16;
    v_stack_m38 = a17;
    result = (unsigned int)(((unsigned int)(a16)) + ((unsigned int)((unsigned int)(a16))));
    v_stack_mE0 = 4;
    v_stack_m30 = (unsigned int)(result);
    v_stack_m28 = a18;
    v_stack_m138 = v_stack_m128;
    v_stack_mC0 = 4;
    v_stack_mB0 = 4;
    v_stack_mA0 = 4;
    v_stack_m90 = 8;
    v_stack_m80 = 4;
    v_stack_m70 = 4;
    v_stack_m60 = 4;
    v_stack_m50 = 8;
    v_stack_m40 = 4;
    v_stack_m20 = 4;
    result = McGenEventWrite_EtwWriteTransfer(v_rip + 8400036, v_rip - 6087761, a3, a2 + 17);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 6087761, a3, a2 + 17);
    v_rsp = (v_rsp) + (336);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t McTemplateU0qqzr1qzr3qqqxqqqpqzr13q_EtwWriteTransfer(int64_t Arg1, int32_t Arg2, int32_t Arg3, void *Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13, int64_t Arg14, int64_t Arg15, uint32_t Arg16, int64_t Arg17, int64_t Arg18)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m128;
    uint64_t v_stack_m138;
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
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;

    v_stack_p20 = (uint32_t)(Arg4);
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (336);
    result = (*(uint64_t *)(v_rip + 0x804B9A)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    v_stack_m110 = 4;
    v_stack_mEC = 0;
    v_stack_m118 = v_stack_p18;
    v_stack_mCC = 0;
    v_stack_m108 = v_stack_p20;
    Arg3 = 0;
    v_stack_mF8 = Arg5;
    v_stack_mF0 = (uint32_t)(Arg4 + Arg4 * 1);
    v_stack_m2C = 0;
    v_stack_mE8 = Arg6;
    v_stack_mD8 = Arg7;
    result = (uint32_t)(((uint32_t)(Arg6)) + ((uint32_t)((uint32_t)(Arg6))));
    v_stack_m100 = 4;
    v_stack_mD0 = (uint32_t)(result);
    v_stack_mC8 = Arg8;
    v_stack_mB8 = Arg9;
    v_stack_mA8 = Arg10;
    v_stack_m98 = Arg11;
    v_stack_m88 = Arg12;
    v_stack_m78 = Arg13;
    v_stack_m68 = Arg14;
    v_stack_m58 = Arg15;
    v_stack_m48 = Arg16;
    v_stack_m38 = Arg17;
    result = (uint32_t)(((uint32_t)(Arg16)) + ((uint32_t)((uint32_t)(Arg16))));
    v_stack_mE0 = 4;
    v_stack_m30 = (uint32_t)(result);
    v_stack_m28 = Arg18;
    v_stack_m138 = v_stack_m128;
    v_stack_mC0 = 4;
    v_stack_mB0 = 4;
    v_stack_mA0 = 4;
    v_stack_m90 = 8;
    v_stack_m80 = 4;
    v_stack_m70 = 4;
    v_stack_m60 = 4;
    v_stack_m50 = 8;
    v_stack_m40 = 4;
    v_stack_m20 = 4;
    result = McGenEventWrite_EtwWriteTransfer(v_rip + 8400036, v_rip - 6087761, Arg3, Arg2 + 17);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 6087761, Arg3, Arg2 + 17);
    local_rsp = (local_rsp) + (336);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0 + r9*1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00605B88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00605B88[BB_00605B88]
  bb_00605D29[BB_00605D29]
```
