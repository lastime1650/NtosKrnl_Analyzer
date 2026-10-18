# EtwpGetSecurityDescriptorByGuid

- RVA: `0x008C04C0`–`0x008C05CB` (길이 `267` bytes)
- VA: `0x00000001408C04C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008345C`
- 디코드: `63`개 명령, `267/267` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x008C0568` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (function, `0x0040FB40`)
- `0x008C057A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x008C0587` → [EtwpGetGuidSecurityDescriptor](EtwpGetGuidSecurityDescriptor_function_008C05D4.md) (function, `0x008C05D4`)
- `0x008C05A9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpAllocGuidEntry](../8B/EtwpAllocGuidEntry_function_008BFF20.md) at `0x008BFFA1`
- [EtwpCheckGuidAccess](EtwpCheckGuidAccess_function_008C697C.md) at `0x008C6996`
- [EtwpStartLogger](../A9/EtwpStartLogger_function_00A99D80.md) at `0x00A9A310`
- [EtwpUpdateTrace](../AB/EtwpUpdateTrace_function_00ABCC7C.md) at `0x00ABD079`
- [EtwpFixBootLoggers](../../init/C4/EtwpFixBootLoggers_function_00C4F09C.md) at `0x00C4F122`

### Static image references
- `0x008C04D5` → RVA `0x00E0A740` (`.data`; read)
- `0x008C0541` → RVA `0x00B06E40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x008C0592` → RVA `0x00E68510` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008C0568` → [RtlStringCbPrintfW](../../text/40/RtlStringCbPrintfW_function_0040FB40.md) (`PAGE` → `.text`)
  - `0x008C057A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x008C05A9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008C04C0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
008C04C5  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
008C04CA  56                              push rsi
008C04CB  57                              push rdi
008C04CC  41 56                           push r14
008C04CE  48 81 EC E0 00 00 00            sub rsp, 0xe0
008C04D5  48 8B 05 64 A2 54 00            mov rax, qword ptr [rip + 0x54a264]
008C04DC  48 33 C4                        xor rax, rsp
008C04DF  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
008C04E7  0F B6 41 0F                     movzx eax, byte ptr [rcx + 0xf]
008C04EB  4C 8B C9                        mov r9, rcx
008C04EE  0F B6 49 0E                     movzx ecx, byte ptr [rcx + 0xe]
008C04F2  48 8B DA                        mov rbx, rdx
008C04F5  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
008C04F9  0F 57 C0                        xorps xmm0, xmm0
008C04FC  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
008C0500  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
008C0508  41 0F B6 51 0D                  movzx edx, byte ptr [r9 + 0xd]
008C050D  45 0F B6 41 0C                  movzx r8d, byte ptr [r9 + 0xc]
008C0512  45 0F B6 51 0B                  movzx r10d, byte ptr [r9 + 0xb]
008C0517  45 0F B6 59 0A                  movzx r11d, byte ptr [r9 + 0xa]
008C051C  41 0F B6 79 09                  movzx edi, byte ptr [r9 + 9]
008C0521  41 0F B6 71 08                  movzx esi, byte ptr [r9 + 8]
008C0526  41 0F B7 69 06                  movzx ebp, word ptr [r9 + 6]
008C052B  45 0F B7 71 04                  movzx r14d, word ptr [r9 + 4]
008C0530  45 8B 09                        mov r9d, dword ptr [r9]
008C0533  89 54 24 58                     mov dword ptr [rsp + 0x58], edx
008C0537  BA 4C 00 00 00                  mov edx, 0x4c
008C053C  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
008C0541  4C 8D 05 F8 68 24 00            lea r8, [rip + 0x2468f8]
008C0548  44 89 54 24 48                  mov dword ptr [rsp + 0x48], r10d
008C054D  44 89 5C 24 40                  mov dword ptr [rsp + 0x40], r11d
008C0552  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
008C0556  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
008C055A  89 6C 24 28                     mov dword ptr [rsp + 0x28], ebp
008C055E  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
008C0563  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
008C0568  E8 D3 F5 B4 FF                  call 0x14040fb40
008C056D  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
008C0575  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
008C057A  E8 01 A2 B6 FF                  call 0x14042a780
008C057F  48 8B D3                        mov rdx, rbx
008C0582  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
008C0587  E8 48 00 00 00                  call 0x1408c05d4
008C058C  48 83 3B 00                     cmp qword ptr [rbx], 0
008C0590  75 35                           jne 0x1408c05c7
008C0592  48 8B 05 77 7F 5A 00            mov rax, qword ptr [rip + 0x5a7f77]
008C0599  48 89 03                        mov qword ptr [rbx], rax
008C059C  32 C0                           xor al, al
008C059E  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
008C05A6  48 33 CC                        xor rcx, rsp
008C05A9  E8 92 C0 DE FF                  call 0x1406ac640
008C05AE  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
008C05B6  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
008C05BA  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
008C05BE  49 8B E3                        mov rsp, r11
008C05C1  41 5E                           pop r14
008C05C3  5F                              pop rdi
008C05C4  5E                              pop rsi
008C05C5  C3                              ret
008C05C6  CC                              int3
008C05C7  B0 01                           mov al, 1
008C05C9  EB D3                           jmp 0x1408c059e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpGetSecurityDescriptorByGuid(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned int v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = v_rbx;
    v_stack_p20 = v_rbp;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 5546596)) ^ (v_rsp);
    v_stack_m28 = result;
    v_stack_m90 = (unsigned int)(*(unsigned __int8 *)(a1 + 15));
    v_stack_m98 = (unsigned int)(*(unsigned __int8 *)(a1 + 14));
    v_stack_mA0 = (unsigned int)(*(unsigned __int8 *)(a1 + 13));
    v_stack_mA8 = (unsigned int)(*(unsigned __int8 *)(a1 + 12));
    v_stack_mB0 = (unsigned int)(*(unsigned __int8 *)(a1 + 11));
    v_stack_mB8 = (unsigned int)(*(unsigned __int8 *)(a1 + 10));
    v_stack_mC0 = (unsigned int)(*(unsigned __int8 *)(a1 + 9));
    v_stack_mC8 = (unsigned int)(*(unsigned __int8 *)(a1 + 8));
    v_stack_mD0 = (unsigned int)(*(unsigned __int16 *)(a1 + 6));
    v_stack_mD8 = (unsigned int)(*(unsigned __int16 *)(a1 + 4));
    v_stack_m88 = v_xmm0;
    result = RtlStringCbPrintfW(v_stack_m78, 76, v_rip + 2386168, (unsigned int)(*(unsigned int *)(a1)));
    result = RtlInitUnicodeString(v_stack_m88, v_stack_m78, v_rip + 2386168, (unsigned int)(*(unsigned int *)(a1)));
    result = EtwpGetGuidSecurityDescriptor(v_stack_m88, a2, v_rip + 2386168, (unsigned int)(*(unsigned int *)(a1)));
    if ((*(unsigned __int64 *)(a2)) != 0) goto loc_008C05C7;
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(v_rip + 5930871);
    result = 0;
loc_008C059E:
    a1 = (v_stack_m28) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_rip + 2386168, (unsigned int)(*(unsigned int *)(a1)));
    return result;
loc_008C05C7:
    goto loc_008C059E;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpGetSecurityDescriptorByGuid(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint32_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = local_rbx;
    v_stack_p20 = local_rbp;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x54A264)) ^ (local_rsp);
    v_stack_m28 = result;
    v_stack_m90 = (uint32_t)(*(uint8_t *)(arg1 + 0xF));
    v_stack_m98 = (uint32_t)(*(uint8_t *)(arg1 + 0xE));
    v_stack_mA0 = (uint32_t)(*(uint8_t *)(arg1 + 0xD));
    v_stack_mA8 = (uint32_t)(*(uint8_t *)(arg1 + 0xC));
    v_stack_mB0 = (uint32_t)(*(uint8_t *)(arg1 + 0xB));
    v_stack_mB8 = (uint32_t)(*(uint8_t *)(arg1 + 0xA));
    v_stack_mC0 = (uint32_t)(*(uint8_t *)(arg1 + 0x9));
    v_stack_mC8 = (uint32_t)(*(uint8_t *)(arg1 + 0x8));
    v_stack_mD0 = (uint32_t)(*(uint16_t *)(arg1 + 0x6));
    v_stack_mD8 = (uint32_t)(*(uint16_t *)(arg1 + 0x4));
    v_stack_m88 = v_xmm0;
    result = RtlStringCbPrintfW(v_stack_m78, 76, v_rip + 2386168, (uint32_t)(*(uint32_t *)(arg1)));
    result = RtlInitUnicodeString(v_stack_m88, v_stack_m78, v_rip + 2386168, (uint32_t)(*(uint32_t *)(arg1)));
    result = EtwpGetGuidSecurityDescriptor(v_stack_m88, Arg2, v_rip + 2386168, (uint32_t)(*(uint32_t *)(arg1)));
    if ((*(uint64_t *)(arg2)) != 0) goto loc_008C05C7;
    *(uint64_t *)(arg2) = *(uint64_t *)(v_rip + 0x5A7F77);
    result = 0;
loc_008C059E:
    Arg1 = (v_stack_m28) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_rip + 2386168, (uint32_t)(*(uint32_t *)(arg1)));
    return result;
loc_008C05C7:
    goto loc_008C059E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `16` | `R` |
| `Arg1` | `+ 0x6` | `16` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x9` | `8` | `R` |
| `Arg1` | `+ 0xA` | `8` | `R` |
| `Arg1` | `+ 0xB` | `8` | `R` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0xD` | `8` | `R` |
| `Arg1` | `+ 0xE` | `8` | `R` |
| `Arg1` | `+ 0xF` | `8` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C04C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008C04C0[BB_008C04C0]
  bb_008C0592[BB_008C0592]
  bb_008C059E[BB_008C059E]
  bb_008C05C6[BB_008C05C6]
  bb_008C05C7[BB_008C05C7]
  bb_008C04C0 -->|branch| bb_008C05C7
  bb_008C04C0 -->|fallthrough| bb_008C0592
  bb_008C0592 -->|flow| bb_008C059E
  bb_008C05C6 -->|flow| bb_008C05C7
  bb_008C05C7 -->|branch| bb_008C059E
```
