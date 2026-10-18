# MiReferenceCfgVad

- RVA: `0x00AABD28`–`0x00AABDE3` (길이 `187` bytes)
- VA: `0x0000000140AABD28`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BBE78`
- 디코드: `53`개 명령, `187/187` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AABD6B` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (function, `0x00316690`)
- `0x00AABD87` → [MiUnlockVadShared](../../text/2E/MiUnlockVadShared_function_002E2420.md) (function, `0x002E2420`)

### Direct callers
- [MmInitializeProcessAddressSpace](../8C/MmInitializeProcessAddressSpace_function_008CF6B0.md) at `0x008CFB55`
- [MmInitializeProcessAddressSpace](../8C/MmInitializeProcessAddressSpace_function_008CF6B0.md) at `0x008CFB6A`
- [MiCfgInitializeProcess](../8D/MiCfgInitializeProcess_function_008D0364.md) at `0x008D03FC`
- [MiCfgInitializeProcess](../8D/MiCfgInitializeProcess_function_008D0364.md) at `0x008D0495`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AABD6B` → [MiObtainReferencedVadEx](../../text/31/MiObtainReferencedVadEx_function_00316690.md) (`PAGE` → `.text`)
  - `0x00AABD87` → [MiUnlockVadShared](../../text/2E/MiUnlockVadShared_function_002E2420.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AABD28  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AABD2D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00AABD32  56                              push rsi
00AABD33  57                              push rdi
00AABD34  41 54                           push r12
00AABD36  41 56                           push r14
00AABD38  41 57                           push r15
00AABD3A  48 83 EC 20                     sub rsp, 0x20
00AABD3E  4C 8B A1 B8 00 00 00            mov r12, qword ptr [rcx + 0xb8]
00AABD45  48 8B EA                        mov rbp, rdx
00AABD48  4D 63 F0                        movsxd r14, r8d
00AABD4B  48 8B F1                        mov rsi, rcx
00AABD4E  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00AABD53  BA 02 00 00 00                  mov edx, 2
00AABD58  48 8B CD                        mov rcx, rbp
00AABD5B  4D 8D 7E 25                     lea r15, [r14 + 0x25]
00AABD5F  49 C1 E7 05                     shl r15, 5
00AABD63  4D 03 BC 24 10 04 00 00         add r15, qword ptr [r12 + 0x410]
00AABD6B  E8 20 A9 86 FF                  call 0x140316690
00AABD70  48 8B D0                        mov rdx, rax
00AABD73  48 8B F8                        mov rdi, rax
00AABD76  8B 48 1C                        mov ecx, dword ptr [rax + 0x1c]
00AABD79  0F B6 58 21                     movzx ebx, byte ptr [rax + 0x21]
00AABD7D  48 C1 E3 20                     shl rbx, 0x20
00AABD81  48 0B D9                        or rbx, rcx
00AABD84  48 8B CE                        mov rcx, rsi
00AABD87  E8 94 66 83 FF                  call 0x1402e2420
00AABD8C  48 C1 E3 0C                     shl rbx, 0xc
00AABD90  33 C0                           xor eax, eax
00AABD92  48 81 CB FF 0F 00 00            or rbx, 0xfff
00AABD99  49 89 2F                        mov qword ptr [r15], rbp
00AABD9C  48 2B DD                        sub rbx, rbp
00AABD9F  49 89 7F 10                     mov qword ptr [r15 + 0x10], rdi
00AABDA3  48 FF C3                        inc rbx
00AABDA6  41 89 47 18                     mov dword ptr [r15 + 0x18], eax
00AABDAA  49 89 5F 08                     mov qword ptr [r15 + 8], rbx
00AABDAE  41 83 FE 01                     cmp r14d, 1
00AABDB2  74 18                           je 0x140aabdcc
00AABDB4  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00AABDB9  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00AABDBE  48 83 C4 20                     add rsp, 0x20
00AABDC2  41 5F                           pop r15
00AABDC4  41 5E                           pop r14
00AABDC6  41 5C                           pop r12
00AABDC8  5F                              pop rdi
00AABDC9  5E                              pop rsi
00AABDCA  C3                              ret
00AABDCB  CC                              int3
00AABDCC  B9 C4 01 00 00                  mov ecx, 0x1c4
00AABDD1  66 41 39 8C 24 EC 06 00 00      cmp word ptr [r12 + 0x6ec], cx
00AABDDA  0F 94 C0                        sete al
00AABDDD  41 89 47 18                     mov dword ptr [r15 + 0x18], eax
00AABDE1  EB D1                           jmp 0x140aabdb4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReferenceCfgVad(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_rsp = (v_rsp) - (32);
    v_r15 = ((int)(a3) + 37) << (5);
    v_r15 = (v_r15) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 1040));
    result = MiObtainReferencedVadEx(a2, 2, v_stack_p18, a4);
    v_rbx = (*(unsigned __int8 *)(result + 33)) << (32);
    v_rbx = (v_rbx) | ((unsigned int)(*(unsigned int *)(result + 28)));
    result = MiUnlockVadShared(a1, result, v_stack_p18, a4);
    v_rbx = (v_rbx) << (12);
    result = 0;
    v_rbx = (v_rbx) | (0xFFFULL);
    *(unsigned __int64 *)(v_r15) = a2;
    v_rbx = (v_rbx) - (a2);
    *(unsigned __int64 *)(v_r15 + 16) = 0;
    v_rbx = (v_rbx) + 1;
    *(unsigned int *)(v_r15 + 24) = 0;
    *(unsigned __int64 *)(v_r15 + 8) = v_rbx;
    if (((unsigned int)((int)(a3))) == 1) goto loc_00AABDCC;
loc_00AABDB4:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00AABDCC:
    result = ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + 1772)) == 452) ? 1 : 0;
    *(unsigned int *)(v_r15 + 24) = (unsigned int)(result);
    goto loc_00AABDB4;
}
```

## 5. (Beta) C Style

```c
int64_t MiReferenceCfgVad(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    local_rsp = (local_rsp) - (32);
    local_r15 = ((int32_t)(Arg3) + 37) << (5);
    local_r15 = (local_r15) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x410));
    result = MiObtainReferencedVadEx(Arg2, 2, v_stack_p18, a4);
    local_rbx = (*(uint8_t *)(result + 0x21)) << (32);
    local_rbx = (local_rbx) | ((uint32_t)(*(uint32_t *)(result + 0x1C)));
    result = MiUnlockVadShared(Arg1, result, v_stack_p18, a4);
    local_rbx = (local_rbx) << (12);
    result = 0;
    local_rbx = (local_rbx) | (0xFFFULL);
    *(uint64_t *)(local_r15) = Arg2;
    local_rbx = (local_rbx) - (Arg2);
    *(uint64_t *)(local_r15 + 0x10) = 0;
    local_rbx = (local_rbx) + 1;
    *(uint32_t *)(local_r15 + 0x18) = 0;
    *(uint64_t *)(local_r15 + 0x8) = local_rbx;
    if (((uint32_t)((int32_t)(Arg3))) == 1) goto loc_00AABDCC;
loc_00AABDB4:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00AABDCC:
    result = ((*(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x6EC)) == 452) ? 1 : 0;
    *(uint32_t *)(local_r15 + 0x18) = (uint32_t)(result);
    goto loc_00AABDB4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg3` | `+ 0x25` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AABD28&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AABD28[BB_00AABD28]
  bb_00AABDB4[BB_00AABDB4]
  bb_00AABDCB[BB_00AABDCB]
  bb_00AABDCC[BB_00AABDCC]
  bb_00AABD28 -->|branch| bb_00AABDCC
  bb_00AABD28 -->|fallthrough| bb_00AABDB4
  bb_00AABDCB -->|flow| bb_00AABDCC
  bb_00AABDCC -->|branch| bb_00AABDB4
```
