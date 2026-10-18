# EtwpStartLoggerThread

- RVA: `0x004B25C4`–`0x004B2677` (길이 `179` bytes)
- VA: `0x00000001404B25C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B9374`
- 디코드: `43`개 명령, `179/179` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004B2637` → [PsCreateSystemThread](../../page/9E/PsCreateSystemThread_function_009ED0D0.md) (function, `0x009ED0D0`)
- `0x004B2656` → [ZwClose](../6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x004B2670` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)

### Direct callers
- [EtwpStartLogger](../../page/A9/EtwpStartLogger_function_00A99D80.md) at `0x00A9ACC4`
- [EtwpFixBootLoggers](../../init/C4/EtwpFixBootLoggers_function_00C4F09C.md) at `0x00C4F184`

### Static image references
- `0x004B25FE` → RVA `0x009BE310` (`EtwpLogger`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004B2637` → [PsCreateSystemThread](../../page/9E/PsCreateSystemThread_function_009ED0D0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B25C4  4C 8B DC                        mov r11, rsp
004B25C7  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
004B25CB  55                              push rbp
004B25CC  48 8B EC                        mov rbp, rsp
004B25CF  48 81 EC 80 00 00 00            sub rsp, 0x80
004B25D6  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
004B25DA  48 8D 45 C0                     lea rax, [rbp - 0x40]
004B25DE  48 83 65 10 00                  and qword ptr [rbp + 0x10], 0
004B25E3  4C 8D 45 D0                     lea r8, [rbp - 0x30]
004B25E7  48 83 65 D8 00                  and qword ptr [rbp - 0x28], 0
004B25EC  48 8B DA                        mov rbx, rdx
004B25EF  48 83 65 E0 00                  and qword ptr [rbp - 0x20], 0
004B25F4  0F 57 C0                        xorps xmm0, xmm0
004B25F7  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
004B25FB  45 33 C9                        xor r9d, r9d
004B25FE  48 8D 05 0B BD 50 00            lea rax, [rip + 0x50bd0b]
004B2605  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
004B2609  48 89 55 C8                     mov qword ptr [rbp - 0x38], rdx
004B260D  48 8D 4D 10                     lea rcx, [rbp + 0x10]
004B2611  49 89 43 A0                     mov qword ptr [r11 - 0x60], rax
004B2615  BA FF FF 1F 00                  mov edx, 0x1fffff
004B261A  49 83 63 98 00                  and qword ptr [r11 - 0x68], 0
004B261F  48 C7 45 D0 30 00 00 00         mov qword ptr [rbp - 0x30], 0x30
004B2627  83 65 D4 00                     and dword ptr [rbp - 0x2c], 0
004B262B  C7 45 E8 00 02 00 00            mov dword ptr [rbp - 0x18], 0x200
004B2632  F3 0F 7F 45 F0                  movdqu xmmword ptr [rbp - 0x10], xmm0
004B2637  E8 94 AA 53 00                  call 0x1409ed0d0
004B263C  85 C0                           test eax, eax
004B263E  79 12                           jns 0x1404b2652
004B2640  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
004B2648  48 81 C4 80 00 00 00            add rsp, 0x80
004B264F  5D                              pop rbp
004B2650  C3                              ret
004B2651  CC                              int3
004B2652  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
004B2656  E8 55 AC 1F 00                  call 0x1406ad2b0
004B265B  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
004B2661  48 8D 8B C8 01 00 00            lea rcx, [rbx + 0x1c8]
004B2668  45 33 C9                        xor r9d, r9d
004B266B  45 33 C0                        xor r8d, r8d
004B266E  33 D2                           xor edx, edx
004B2670  E8 3B C0 D5 FF                  call 0x14020e6b0
004B2675  EB C9                           jmp 0x1404b2640
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpStartLoggerThread(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    v_rsp = (v_rsp) - (128);
    *(unsigned __int64 *)(v_rsp - 88) = v_stack_m48;
    a4 = 0;
    v_stack_m48 = a1;
    v_stack_m40 = a2;
    *(unsigned __int64 *)(v_rsp - 96) = v_rip + 5291275;
    v_stack_m38 = 48;
    v_stack_m20 = 512;
    v_stack_m18 = v_xmm0;
    result = PsCreateSystemThread(v_stack_p8, (unsigned int)(0x1FFFFFULL), v_stack_m38, a4);
    if (!sign_flag) goto loc_004B2652;
loc_004B2640:
    v_rsp = (v_rsp) + (128);
    return result;
loc_004B2652:
    result = ZwClose(v_stack_p8, (unsigned int)(0x1FFFFFULL), v_stack_m38, a4);
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_stack_p10 + 456, a2, a3, a4);
    goto loc_004B2640;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpStartLoggerThread(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    local_rsp = (local_rsp) - (128);
    *(uint64_t *)(local_rsp - 0x58) = v_stack_m48;
    Arg4 = 0;
    v_stack_m48 = Arg1;
    v_stack_m40 = Arg2;
    *(uint64_t *)(local_rsp - 0x60) = v_rip + 5291275;
    v_stack_m38 = 48;
    v_stack_m20 = 512;
    v_stack_m18 = v_xmm0;
    result = PsCreateSystemThread(v_stack_p8, (uint32_t)(0x1FFFFFULL), v_stack_m38, Arg4);
    if (!sign_flag) goto loc_004B2652;
loc_004B2640:
    local_rsp = (local_rsp) + (128);
    return result;
loc_004B2652:
    result = ZwClose(v_stack_p8, (uint32_t)(0x1FFFFFULL), v_stack_m38, Arg4);
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_stack_p10 + 456, Arg2, Arg3, Arg4);
    goto loc_004B2640;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x1C8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B25C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B25C4[BB_004B25C4]
  bb_004B2640[BB_004B2640]
  bb_004B2651[BB_004B2651]
  bb_004B2652[BB_004B2652]
  bb_004B25C4 -->|branch| bb_004B2652
  bb_004B25C4 -->|fallthrough| bb_004B2640
  bb_004B2651 -->|flow| bb_004B2652
  bb_004B2652 -->|branch| bb_004B2640
```
