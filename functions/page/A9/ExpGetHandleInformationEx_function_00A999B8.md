# ExpGetHandleInformationEx

- RVA: `0x00A999B8`–`0x00A99A48` (길이 `144` bytes)
- VA: `0x0000000140A999B8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B8C90`
- 디코드: `40`개 명령, `144/144` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A99A0C` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x00A99A33` → [ObGetHandleInformationEx](ObGetHandleInformationEx_function_00A99A50.md) (function, `0x00A99A50`)
- `0x00A99A3F` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (function, `0x0029F258`)

### Direct callers
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A58B92`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A99A3F` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A999B8  4C 8B DC                        mov r11, rsp
00A999BB  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00A999BF  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
00A999C3  57                              push rdi
00A999C4  48 83 EC 40                     sub rsp, 0x40
00A999C8  41 83 21 00                     and dword ptr [r9], 0
00A999CC  41 8B F8                        mov edi, r8d
00A999CF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A999D8  4C 8B D2                        mov r10, rdx
00A999DB  49 83 63 20 00                  and qword ptr [r11 + 0x20], 0
00A999E0  49 8B D9                        mov rbx, r9
00A999E3  49 83 63 E8 00                  and qword ptr [r11 - 0x18], 0
00A999E8  8B F1                           mov esi, ecx
00A999EA  41 B9 01 00 00 00               mov r9d, 1
00A999F0  8B D7                           mov edx, edi
00A999F2  44 8A 80 32 02 00 00            mov r8b, byte ptr [rax + 0x232]
00A999F9  49 8B CA                        mov rcx, r10
00A999FC  49 8D 43 E8                     lea rax, [r11 - 0x18]
00A99A00  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00A99A04  49 8D 43 20                     lea rax, [r11 + 0x20]
00A99A08  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00A99A0C  E8 A7 99 EB FF                  call 0x1409533b8
00A99A11  85 C0                           test eax, eax
00A99A13  79 11                           jns 0x140a99a26
00A99A15  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00A99A1A  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
00A99A1F  48 83 C4 40                     add rsp, 0x40
00A99A23  5F                              pop rdi
00A99A24  C3                              ret
00A99A25  CC                              int3
00A99A26  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00A99A2B  4C 8B CB                        mov r9, rbx
00A99A2E  44 8B C7                        mov r8d, edi
00A99A31  8B CE                           mov ecx, esi
00A99A33  E8 18 00 00 00                  call 0x140a99a50
00A99A38  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00A99A3D  8B D8                           mov ebx, eax
00A99A3F  E8 14 58 80 FF                  call 0x14029f258
00A99A44  8B C3                           mov eax, ebx
00A99A46  EB CD                           jmp 0x140a99a15
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpGetHandleInformationEx(int a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 32) = v_rsp - 24;
    *(unsigned __int64 *)(v_rsp - 40) = v_rsp + 32;
    result = ExLockUserBuffer(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), 1);
    if (!sign_flag) goto loc_00A99A26;
loc_00A99A15:
    v_rsp = (v_rsp) + (64);
    return result;
loc_00A99A26:
    result = ObGetHandleInformationEx((unsigned int)((unsigned int)(v_stack_p10)), v_stack_p68, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_p8);
    result = ExUnlockUserBuffer(v_stack_p30, v_stack_p68, (unsigned int)((unsigned int)((unsigned int)(a3))), v_stack_p8);
    goto loc_00A99A15;
}
```

## 5. (Beta) C Style

```c
int64_t ExpGetHandleInformationEx(int32_t Arg1, int64_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p30;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x20) = local_rsp - 24;
    *(uint64_t *)(local_rsp - 0x28) = local_rsp + 32;
    result = ExLockUserBuffer(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), 1);
    if (!sign_flag) goto loc_00A99A26;
loc_00A99A15:
    local_rsp = (local_rsp) + (64);
    return result;
loc_00A99A26:
    result = ObGetHandleInformationEx((uint32_t)((uint32_t)(v_stack_p10)), v_stack_p68, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_p8);
    result = ExUnlockUserBuffer(v_stack_p30, v_stack_p68, (uint32_t)((uint32_t)((uint32_t)(Arg3))), v_stack_p8);
    goto loc_00A99A15;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A999B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A999B8[BB_00A999B8]
  bb_00A99A15[BB_00A99A15]
  bb_00A99A25[BB_00A99A25]
  bb_00A99A26[BB_00A99A26]
  bb_00A999B8 -->|branch| bb_00A99A26
  bb_00A999B8 -->|fallthrough| bb_00A99A15
  bb_00A99A25 -->|flow| bb_00A99A26
  bb_00A99A26 -->|branch| bb_00A99A15
```
