# WheaInitializeRegChangeNotify

- RVA: `0x007D89BC`–`0x007D8A46` (길이 `138` bytes)
- VA: `0x00000001407D89BC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD5F0`
- 디코드: `32`개 명령, `138/138` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x007D8A30` → [NtNotifyChangeMultipleKeys](../9D/NtNotifyChangeMultipleKeys_function_009DC6B0.md) (function, `0x009DC6B0`)

### Direct callers
- [WheapSetPolicyValue](WheapSetPolicyValue_function_007D8E3C.md) at `0x007D8E6F`
- [WheaInitialize](../../init/C5/WheaInitialize_function_00C54C08.md) at `0x00C55118`

### Static image references
- `0x007D89C4` → RVA `0x00EF7D38` (`.data`; read)
- `0x007D89D0` → RVA `0x00EF7D58` (`.data`; read/write)
- `0x007D89D8` → RVA `0x007D8A50` (`WheaRegChangeNotifyCallback`; read)
- `0x007D89DF` → RVA `0x00EF7D40` (`.data`; read/write)
- `0x007D8A07` → RVA `0x00EF7D50` (`.data`; write)
- `0x007D8A0E` → RVA `0x00EF7D60` (`.data`; read)
- `0x007D8A21` → RVA `0x00EF7D40` (`.data`; read)
- `0x007D8A39` → RVA `0x00EF7D30` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D89BC  4C 8B DC                        mov r11, rsp
007D89BF  53                              push rbx
007D89C0  48 83 EC 60                     sub rsp, 0x60
007D89C4  48 8B 0D 6D F3 71 00            mov rcx, qword ptr [rip + 0x71f36d]
007D89CB  48 85 C9                        test rcx, rcx
007D89CE  74 6F                           je 0x1407d8a3f
007D89D0  48 83 25 80 F3 71 00 00         and qword ptr [rip + 0x71f380], 0
007D89D8  48 8D 05 71 00 00 00            lea rax, [rip + 0x71]
007D89DF  48 83 25 59 F3 71 00 00         and qword ptr [rip + 0x71f359], 0
007D89E7  BB 01 00 00 00                  mov ebx, 1
007D89EC  88 5C 24 58                     mov byte ptr [rsp + 0x58], bl
007D89F0  45 33 C9                        xor r9d, r9d
007D89F3  83 64 24 50 00                  and dword ptr [rsp + 0x50], 0
007D89F8  45 33 C0                        xor r8d, r8d
007D89FB  49 83 63 E0 00                  and qword ptr [r11 - 0x20], 0
007D8A00  33 D2                           xor edx, edx
007D8A02  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
007D8A07  48 89 05 42 F3 71 00            mov qword ptr [rip + 0x71f342], rax
007D8A0E  48 8D 05 4B F3 71 00            lea rax, [rip + 0x71f34b]
007D8A15  C7 44 24 38 04 00 00 00         mov dword ptr [rsp + 0x38], 4
007D8A1D  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
007D8A21  48 8D 05 18 F3 71 00            lea rax, [rip + 0x71f318]
007D8A28  49 89 5B C0                     mov qword ptr [r11 - 0x40], rbx
007D8A2C  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
007D8A30  E8 7B 3C 20 00                  call 0x1409dc6b0
007D8A35  85 C0                           test eax, eax
007D8A37  79 06                           jns 0x1407d8a3f
007D8A39  87 1D F1 F2 71 00               xchg dword ptr [rip + 0x71f2f1], ebx
007D8A3F  48 83 C4 60                     add rsp, 0x60
007D8A43  5B                              pop rbx
007D8A44  C3                              ret
007D8A45  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheaInitializeRegChangeNotify(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned __int8 v_stack_m28;
    unsigned int v_stack_m30;

    v_rsp = (v_rsp) - (96);
    if (*(unsigned __int64 *)(v_rip + 7467885) == 0) goto loc_007D8A3F;
    v_stack_m10 = 1;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    v_stack_m28 = 0;
    *(unsigned __int64 *)(v_rip + 7467842) = v_rip + 113;
    v_stack_m30 = 4;
    *(unsigned __int64 *)(v_rsp - 56) = v_rip + 7467851;
    *(unsigned __int64 *)(v_rsp - 64) = 1;
    *(unsigned __int64 *)(v_rsp - 72) = v_rip + 7467800;
    result = NtNotifyChangeMultipleKeys(*(unsigned __int64 *)(v_rip + 7467885), a2, a3, a4);
    if (sign_flag) {
    }
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WheaInitializeRegChangeNotify(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m10;
    uint32_t v_stack_m18;
    uint8_t v_stack_m28;
    uint32_t v_stack_m30;

    local_rsp = (local_rsp) - (96);
    if (*(uint64_t *)(v_rip + 0x71F36D) == 0) goto loc_007D8A3F;
    v_stack_m10 = 1;
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m28 = 0;
    *(uint64_t *)(v_rip + 0x71F342) = v_rip + 113;
    v_stack_m30 = 4;
    *(uint64_t *)(local_rsp - 0x38) = v_rip + 7467851;
    *(uint64_t *)(local_rsp - 0x40) = 1;
    *(uint64_t *)(local_rsp - 0x48) = v_rip + 7467800;
    result = NtNotifyChangeMultipleKeys(*(uint64_t *)(v_rip + 0x71F36D), Arg2, Arg3, Arg4);
    if (sign_flag) {
    }
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D89BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007D89BC[BB_007D89BC]
  bb_007D89D0[BB_007D89D0]
  bb_007D8A39[BB_007D8A39]
  bb_007D8A3F[BB_007D8A3F]
  bb_007D8A45[BB_007D8A45]
  bb_007D89BC -->|branch| bb_007D8A3F
  bb_007D89BC -->|fallthrough| bb_007D89D0
  bb_007D89D0 -->|branch| bb_007D8A3F
  bb_007D89D0 -->|fallthrough| bb_007D8A39
  bb_007D8A39 -->|flow| bb_007D8A3F
```
