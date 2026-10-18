# PpIrpAllocateDeviceUsageNotification

- RVA: `0x0073E1DC`–`0x0073E283` (길이 `167` bytes)
- VA: `0x000000014073E1DC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `43`개 명령, `167/167` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0073E1F5` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (function, `0x0040DD10`)
- `0x0073E202` → [IoAllocateIrp](../../text/20/IoAllocateIrp_function_002065D0.md) (function, `0x002065D0`)

### Direct callers
- [PiPagePathSetState](../72/PiPagePathSetState_function_0072BDE0.md) at `0x0072BE38`
- [PipSendGuestAssignedNotification](../74/PipSendGuestAssignedNotification_function_007404B4.md) at `0x007404F4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0073E1F5` → [KeInitializeEvent](../../text/40/KeInitializeEvent_function_0040DD10.md) (`PAGE` → `.text`)
  - `0x0073E202` → [IoAllocateIrp](../../text/20/IoAllocateIrp_function_002065D0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0073E1DC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0073E1E1  57                              push rdi
0073E1E2  48 83 EC 20                     sub rsp, 0x20
0073E1E6  48 8D 79 28                     lea rdi, [rcx + 0x28]
0073E1EA  48 8B D9                        mov rbx, rcx
0073E1ED  48 8B CF                        mov rcx, rdi
0073E1F0  45 33 C0                        xor r8d, r8d
0073E1F3  33 D2                           xor edx, edx
0073E1F5  E8 16 FB CC FF                  call 0x14040dd10
0073E1FA  48 8B 0B                        mov rcx, qword ptr [rbx]
0073E1FD  33 D2                           xor edx, edx
0073E1FF  8A 49 4C                        mov cl, byte ptr [rcx + 0x4c]
0073E202  E8 C9 83 AC FF                  call 0x1402065d0
0073E207  45 33 C0                        xor r8d, r8d
0073E20A  48 8B D0                        mov rdx, rax
0073E20D  48 85 C0                        test rax, rax
0073E210  74 62                           je 0x14073e274
0073E212  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0073E216  48 89 88 C0 00 00 00            mov qword ptr [rax + 0xc0], rcx
0073E21D  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0073E226  48 89 88 98 00 00 00            mov qword ptr [rax + 0x98], rcx
0073E22D  48 8D 4B 18                     lea rcx, [rbx + 0x18]
0073E231  48 89 48 48                     mov qword ptr [rax + 0x48], rcx
0073E235  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0073E23C  44 88 40 40                     mov byte ptr [rax + 0x40], r8b
0073E240  48 89 78 50                     mov qword ptr [rax + 0x50], rdi
0073E244  C7 40 10 04 00 00 00            mov dword ptr [rax + 0x10], 4
0073E24B  4C 89 40 58                     mov qword ptr [rax + 0x58], r8
0073E24F  66 C7 41 B8 1B 16               mov word ptr [rcx - 0x48], 0x161b
0073E255  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0073E259  48 89 41 E8                     mov qword ptr [rcx - 0x18], rax
0073E25D  C7 42 30 BB 00 00 C0            mov dword ptr [rdx + 0x30], 0xc00000bb
0073E264  4C 89 42 18                     mov qword ptr [rdx + 0x18], r8
0073E268  8A 43 0C                        mov al, byte ptr [rbx + 0xc]
0073E26B  88 41 C0                        mov byte ptr [rcx - 0x40], al
0073E26E  8B 43 08                        mov eax, dword ptr [rbx + 8]
0073E271  89 41 C8                        mov dword ptr [rcx - 0x38], eax
0073E274  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0073E279  48 8B C2                        mov rax, rdx
0073E27C  48 83 C4 20                     add rsp, 0x20
0073E280  5F                              pop rdi
0073E281  C3                              ret
0073E282  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpIrpAllocateDeviceUsageNotification(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeInitializeEvent(a1 + 40, a2, a3, a4);
    a2 = 0;
    result = IoAllocateIrp(*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 76), a2, a3, a4);
    a3 = 0;
    if (result != 0) {
        a1 = *(unsigned __int64 *)(a1 + 16);
        *(unsigned __int64 *)(result + 192) = a1;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        *(unsigned __int64 *)(result + 152) = a1;
        a1 = a1 + 24;
        *(unsigned __int64 *)(result + 72) = a1;
        a1 = *(unsigned __int64 *)(result + 184);
        *(unsigned __int8 *)(result + 64) = 0;
        *(unsigned __int64 *)(result + 80) = a1 + 40;
        *(unsigned int *)(result + 16) = 4;
        *(unsigned __int64 *)(result + 88) = 0;
        *(unsigned __int16 *)(a1 - 72) = 0x161BULL;
        result = *(unsigned __int64 *)(a1 + 16);
        *(unsigned __int64 *)(a1 - 24) = result;
        *(unsigned int *)(result + 48) = 0xC00000BBULL;
        *(unsigned __int64 *)(result + 24) = 0;
        result = *(unsigned __int8 *)(a1 + 12);
        *(unsigned __int8 *)(a1 - 64) = (unsigned __int8)(result);
        result = *(unsigned int *)(a1 + 8);
        *(unsigned int *)(a1 - 56) = (unsigned int)(result);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpIrpAllocateDeviceUsageNotification(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeInitializeEvent(Arg1 + 40, Arg2, Arg3, a4);
    Arg2 = 0;
    result = IoAllocateIrp(*(uint8_t *)(*(uint64_t *)(arg1) + 0x4C), Arg2, Arg3, a4);
    Arg3 = 0;
    if (result != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x10);
        *(void **)(result + 0xC0) = Arg1;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        *(void **)(result + 0x98) = Arg1;
        Arg1 = Arg1 + 24;
        *(void **)(result + 0x48) = Arg1;
        Arg1 = *(uint64_t *)(result + 0xB8);
        *(uint8_t *)(result + 0x40) = 0;
        *(void **)(result + 0x50) = Arg1 + 40;
        *(uint32_t *)(result + 0x10) = 4;
        *(uint64_t *)(result + 0x58) = 0;
        *(uint16_t *)(arg1 - 0x48) = 0x161BULL;
        result = *(uint64_t *)(arg1 + 0x10);
        *(uint64_t *)(arg1 - 0x18) = result;
        *(uint32_t *)(result + 0x30) = 0xC00000BBULL;
        *(uint64_t *)(result + 0x18) = 0;
        result = *(uint8_t *)(arg1 + 0xC);
        *(uint8_t *)(arg1 - 0x40) = (uint8_t)(result);
        result = *(uint32_t *)(arg1 + 0x8);
        *(uint32_t *)(arg1 - 0x38) = (uint32_t)(result);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0073E1DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0073E1DC[BB_0073E1DC]
  bb_0073E212[BB_0073E212]
  bb_0073E274[BB_0073E274]
  bb_0073E282[BB_0073E282]
  bb_0073E1DC -->|branch| bb_0073E274
  bb_0073E1DC -->|fallthrough| bb_0073E212
  bb_0073E212 -->|flow| bb_0073E274
```
