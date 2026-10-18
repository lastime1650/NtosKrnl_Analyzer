# IoCreateFileSpecifyDeviceObjectHint

- RVA: `0x00A6D4B0`–`0x00A6D573` (길이 `195` bytes)
- VA: `0x0000000140A6D4B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B461C`
- 디코드: `38`개 명령, `195/195` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A6D565` → [IoCreateFileEx](../8A/IoCreateFileEx_function_008AB000.md) (function, `0x008AB000`)

### Direct callers
- [DifIoCreateFileSpecifyDeviceObjectHintWrapper](../../text/62/DifIoCreateFileSpecifyDeviceObjectHintWrapper_function_00629070.md) at `0x00629220`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A6D4B0  4C 8B DC                        mov r11, rsp
00A6D4B3  48 81 EC B8 00 00 00            sub rsp, 0xb8
00A6D4BA  33 C0                           xor eax, eax
00A6D4BC  49 C7 43 E8 01 00 00 00         mov qword ptr [r11 - 0x18], 1
00A6D4C4  49 89 43 CA                     mov qword ptr [r11 - 0x36], rax
00A6D4C8  41 89 43 D2                     mov dword ptr [r11 - 0x2e], eax
00A6D4CC  66 41 89 43 D6                  mov word ptr [r11 - 0x2a], ax
00A6D4D1  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00A6D4D5  B8 28 00 00 00                  mov eax, 0x28
00A6D4DA  66 41 89 43 C8                  mov word ptr [r11 - 0x38], ax
00A6D4DF  48 8B 84 24 30 01 00 00         mov rax, qword ptr [rsp + 0x130]
00A6D4E7  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00A6D4EB  49 8D 43 C8                     lea rax, [r11 - 0x38]
00A6D4EF  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
00A6D4F3  8B 84 24 28 01 00 00            mov eax, dword ptr [rsp + 0x128]
00A6D4FA  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00A6D4FE  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
00A6D506  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
00A6D50A  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
00A6D511  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00A6D515  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
00A6D51C  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00A6D520  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
00A6D528  49 89 43 90                     mov qword ptr [r11 - 0x70], rax
00A6D52C  8B 84 24 00 01 00 00            mov eax, dword ptr [rsp + 0x100]
00A6D533  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A6D537  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
00A6D53E  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00A6D542  8B 84 24 F0 00 00 00            mov eax, dword ptr [rsp + 0xf0]
00A6D549  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A6D54D  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
00A6D554  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00A6D558  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00A6D560  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A6D565  E8 96 DA E3 FF                  call 0x1408ab000
00A6D56A  48 81 C4 B8 00 00 00            add rsp, 0xb8
00A6D571  C3                              ret
00A6D572  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoCreateFileSpecifyDeviceObjectHint(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, __int64 a10, unsigned int a11, unsigned int a12, __int64 a13, unsigned int a14, __int64 a15)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m50;
    unsigned int v_stack_m60;
    unsigned int v_stack_m68;
    unsigned int v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;

    v_rsp = (v_rsp) - (184);
    result = 0;
    *(unsigned __int64 *)(v_rsp - 24) = 1;
    *(unsigned __int64 *)(v_rsp - 54) = 0;
    *(unsigned int *)(v_rsp - 46) = 0;
    *(unsigned __int16 *)(v_rsp - 42) = 0;
    *(unsigned __int64 *)(v_rsp - 32) = 0;
    *(unsigned __int16 *)(v_rsp - 56) = 40;
    *(unsigned __int64 *)(v_rsp - 40) = a15;
    *(unsigned __int64 *)(v_rsp - 72) = v_rsp - 56;
    v_stack_m50 = (unsigned int)((unsigned int)(a14));
    *(unsigned __int64 *)(v_rsp - 88) = a13;
    v_stack_m60 = (unsigned int)((unsigned int)(a12));
    v_stack_m68 = (unsigned int)((unsigned int)(a11));
    *(unsigned __int64 *)(v_rsp - 112) = a10;
    v_stack_m78 = (unsigned int)((unsigned int)(a9));
    v_stack_m80 = (unsigned int)((unsigned int)(a8));
    v_stack_m88 = (unsigned int)((unsigned int)(a7));
    v_stack_m90 = (unsigned int)((unsigned int)(a6));
    v_stack_m98 = a5;
    result = IoCreateFileEx(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (184);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoCreateFileSpecifyDeviceObjectHint(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, uint32_t Arg8, uint32_t Arg9, int64_t Arg10, uint32_t Arg11, uint32_t Arg12, int64_t Arg13, uint32_t Arg14, int64_t Arg15)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m50;
    uint32_t v_stack_m60;
    uint32_t v_stack_m68;
    uint32_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;

    local_rsp = (local_rsp) - (184);
    result = 0;
    *(uint64_t *)(local_rsp - 0x18) = 1;
    *(uint64_t *)(local_rsp - 0x36) = 0;
    *(uint32_t *)(local_rsp - 0x2E) = 0;
    *(uint16_t *)(local_rsp - 0x2A) = 0;
    *(uint64_t *)(local_rsp - 0x20) = 0;
    *(uint16_t *)(local_rsp - 0x38) = 40;
    *(uint64_t *)(local_rsp - 0x28) = Arg15;
    *(uint64_t *)(local_rsp - 0x48) = local_rsp - 56;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg14));
    *(uint64_t *)(local_rsp - 0x58) = Arg13;
    v_stack_m60 = (uint32_t)((uint32_t)(Arg12));
    v_stack_m68 = (uint32_t)((uint32_t)(Arg11));
    *(uint64_t *)(local_rsp - 0x70) = Arg10;
    v_stack_m78 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m80 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m88 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m90 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m98 = Arg5;
    result = IoCreateFileEx(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (184);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A6D4B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A6D4B0[BB_00A6D4B0]
  bb_00A6D572[BB_00A6D572]
```
