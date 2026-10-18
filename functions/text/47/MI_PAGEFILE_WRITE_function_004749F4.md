# MI_PAGEFILE_WRITE

- RVA: `0x004749F4`–`0x00474B39` (길이 `325` bytes)
- VA: `0x00000001404749F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000950EC`
- 디코드: `53`개 명령, `325/325` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiGatherPagefilePages](../37/MiGatherPagefilePages_function_00372B08.md) at `0x00372EDB`
- [MiWriteComplete](../40/MiWriteComplete_function_004069B0.md) at `0x00406DE3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004749F4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004749F9  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
004749FE  4C 8B 51 40                     mov r10, qword ptr [rcx + 0x40]
00474A02  48 8B F9                        mov rdi, rcx
00474A05  41 BB 01 00 00 00               mov r11d, 1
00474A0B  49 8B 9A D8 00 00 00            mov rbx, qword ptr [r10 + 0xd8]
00474A12  F0 44 0F C1 9B 00 4D 00 00      lock xadd dword ptr [rbx + 0x4d00], r11d
00474A1B  8B 44 24 28                     mov eax, dword ptr [rsp + 0x28]
00474A1F  41 FF C3                        inc r11d
00474A22  41 83 E3 1F                     and r11d, 0x1f
00474A26  49 C1 E3 07                     shl r11, 7
00474A2A  45 85 C9                        test r9d, r9d
00474A2D  41 89 84 1B 08 4D 00 00         mov dword ptr [r11 + rbx + 0x4d08], eax
00474A35  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00474A3E  8A 88 C3 00 00 00               mov cl, byte ptr [rax + 0xc3]
00474A44  0F 95 C0                        setne al
00474A47  41 88 84 1B 0F 4D 00 00         mov byte ptr [r11 + rbx + 0x4d0f], al
00474A4F  41 88 8C 1B 0D 4D 00 00         mov byte ptr [r11 + rbx + 0x4d0d], cl
00474A57  45 88 84 1B 0E 4D 00 00         mov byte ptr [r11 + rbx + 0x4d0e], r8b
00474A5F  49 89 94 1B 10 4D 00 00         mov qword ptr [r11 + rbx + 0x4d10], rdx
00474A67  41 8A 82 AC 00 00 00            mov al, byte ptr [r10 + 0xac]
00474A6E  24 0F                           and al, 0xf
00474A70  41 88 84 1B 0C 4D 00 00         mov byte ptr [r11 + rbx + 0x4d0c], al
00474A78  48 8B 83 00 49 00 00            mov rax, qword ptr [rbx + 0x4900]
00474A7F  49 89 84 1B 18 4D 00 00         mov qword ptr [r11 + rbx + 0x4d18], rax
00474A87  48 8B 83 C0 4B 00 00            mov rax, qword ptr [rbx + 0x4bc0]
00474A8E  49 89 84 1B 20 4D 00 00         mov qword ptr [r11 + rbx + 0x4d20], rax
00474A96  48 8B 83 A0 4C 00 00            mov rax, qword ptr [rbx + 0x4ca0]
00474A9D  49 89 84 1B 28 4D 00 00         mov qword ptr [r11 + rbx + 0x4d28], rax
00474AA5  48 8B 83 40 4C 00 00            mov rax, qword ptr [rbx + 0x4c40]
00474AAC  49 89 84 1B 30 4D 00 00         mov qword ptr [r11 + rbx + 0x4d30], rax
00474AB4  41 0F B7 82 AC 00 00 00         movzx eax, word ptr [r10 + 0xac]
00474ABC  83 E0 0F                        and eax, 0xf
00474ABF  48 83 C0 30                     add rax, 0x30
00474AC3  48 6B C0 58                     imul rax, rax, 0x58
00474AC7  48 8B 04 18                     mov rax, qword ptr [rax + rbx]
00474ACB  49 89 84 1B 48 4D 00 00         mov qword ptr [r11 + rbx + 0x4d48], rax
00474AD3  48 8B 83 80 0F 00 00            mov rax, qword ptr [rbx + 0xf80]
00474ADA  49 89 84 1B 38 4D 00 00         mov qword ptr [r11 + rbx + 0x4d38], rax
00474AE2  48 8B 83 00 10 00 00            mov rax, qword ptr [rbx + 0x1000]
00474AE9  49 89 84 1B 40 4D 00 00         mov qword ptr [r11 + rbx + 0x4d40], rax
00474AF1  0F 10 47 68                     movups xmm0, xmmword ptr [rdi + 0x68]
00474AF5  41 0F 11 84 1B 50 4D 00 00      movups xmmword ptr [r11 + rbx + 0x4d50], xmm0
00474AFE  0F 10 4F 78                     movups xmm1, xmmword ptr [rdi + 0x78]
00474B02  41 0F 11 8C 1B 60 4D 00 00      movups xmmword ptr [r11 + rbx + 0x4d60], xmm1
00474B0B  0F 10 87 88 00 00 00            movups xmm0, xmmword ptr [rdi + 0x88]
00474B12  41 0F 11 84 1B 70 4D 00 00      movups xmmword ptr [r11 + rbx + 0x4d70], xmm0
00474B1B  F2 0F 10 8F 98 00 00 00         movsd xmm1, qword ptr [rdi + 0x98]
00474B23  48 8B 7C 24 10                  mov rdi, qword ptr [rsp + 0x10]
00474B28  F2 41 0F 11 8C 1B 80 4D 00 00   movsd qword ptr [r11 + rbx + 0x4d80], xmm1
00474B32  48 8B 5C 24 08                  mov rbx, qword ptr [rsp + 8]
00474B37  C3                              ret
00474B38  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MI_PAGEFILE_WRITE(__int64 a1, __int64 a2, unsigned __int8 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r11;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    v_r11 = (unsigned int)((1) + 1);
    v_r11 = (unsigned int)((v_r11) & (31));
    v_r11 = (v_r11) << (7);
    *(unsigned int *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19720) = (unsigned int)((unsigned int)(a5));
    result = (a4 != 0) ? 1 : 0;
    *(unsigned __int8 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19727) = (unsigned __int8)(result);
    *(unsigned __int8 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19725) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 195));
    *(unsigned __int8 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19726) = a3;
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19728) = a2;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 64) + 172)) & (15));
    *(unsigned __int8 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19724) = (unsigned __int8)(result);
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19736) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 18688);
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19744) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 19392);
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19752) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 19616);
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19760) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 19520);
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 64) + 172)) & (15));
    result = (result) + (48);
    result = (result) * (result);
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19784) = *(unsigned __int64 *)(result + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1);
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19768) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 3968);
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19776) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 4096);
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19792) = v_xmm0;
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19808) = v_xmm1;
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19824) = v_xmm0;
    *(unsigned __int64 *)(v_r11 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) * 1 + 19840) = v_xmm1;
    return *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 64) + 216) + 4096);
}
```

## 5. (Beta) C Style

```c
int64_t MI_PAGEFILE_WRITE(void *Arg1, int64_t Arg2, uint8_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    local_r11 = (uint32_t)((1) + 1);
    local_r11 = (uint32_t)((local_r11) & (31));
    local_r11 = (local_r11) << (7);
    *(uint32_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D08) = (uint32_t)((uint32_t)(Arg5));
    result = (Arg4 != 0) ? 1 : 0;
    *(uint8_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D0F) = (uint8_t)(result);
    *(uint8_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D0D) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xC3));
    *(uint8_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D0E) = Arg3;
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D10) = Arg2;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0x40) + 0xAC)) & (15));
    *(uint8_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D0C) = (uint8_t)(result);
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D18) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4900);
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D20) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4BC0);
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D28) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4CA0);
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D30) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x4C40);
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(arg1 + 0x40) + 0xAC)) & (15));
    result = (result) + (48);
    result = (result) * (result);
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D48) = *(uint64_t *)(result + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1);
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D38) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0xF80);
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D40) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x1000);
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D50) = v_xmm0;
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D60) = v_xmm1;
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D70) = v_xmm0;
    *(uint64_t *)(local_r11 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) * 1 + 0x4D80) = v_xmm1;
    return *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x40) + 0xD8) + 0x1000);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x68` | `128` | `R` |
| `Arg1` | `+ 0x78` | `128` | `R` |
| `Arg1` | `+ 0x88` | `128` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004749F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004749F4[BB_004749F4]
  bb_00474B38[BB_00474B38]
```
