# SdbpMatchOem

- RVA: `0x008168C8`–`0x00816971` (길이 `169` bytes)
- VA: `0x00000001408168C8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009B270`
- 디코드: `47`개 명령, `169/169` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008168EB` → [SdbFindFirstTag](../95/SdbFindFirstTag_function_0095E34C.md) (function, `0x0095E34C`)
- `0x0081690A` → [SdbpMatchDeviceString](SdbpMatchDeviceString_function_008166C4.md) (function, `0x008166C4`)
- `0x00816923` → [SdbpMatchDeviceString](SdbpMatchDeviceString_function_008166C4.md) (function, `0x008166C4`)
- `0x00816949` → [SdbpMatchDeviceDWORD](SdbpMatchDeviceDWORD_function_00816638.md) (function, `0x00816638`)

### Direct callers
- [SdbpCheckKObject](../95/SdbpCheckKObject_function_00959F04.md) at `0x00959FEC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008168C8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008168CD  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
008168D2  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
008168D7  41 56                           push r14
008168D9  48 83 EC 30                     sub rsp, 0x30
008168DD  4D 8B F0                        mov r14, r8
008168E0  48 8B F9                        mov rdi, rcx
008168E3  41 B8 22 70 00 00               mov r8d, 0x7022
008168E9  33 DB                           xor ebx, ebx
008168EB  E8 5C 7A 14 00                  call 0x14095e34c
008168F0  8B F0                           mov esi, eax
008168F2  85 C0                           test eax, eax
008168F4  75 05                           jne 0x1408168fb
008168F6  8D 58 01                        lea ebx, [rax + 1]
008168F9  EB 5D                           jmp 0x140816958
008168FB  49 8B 16                        mov rdx, qword ptr [r14]
008168FE  41 B9 25 60 00 00               mov r9d, 0x6025
00816904  44 8B C6                        mov r8d, esi
00816907  48 8B CF                        mov rcx, rdi
0081690A  E8 B5 FD FF FF                  call 0x1408166c4
0081690F  85 C0                           test eax, eax
00816911  74 45                           je 0x140816958
00816913  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
00816917  41 B9 26 60 00 00               mov r9d, 0x6026
0081691D  44 8B C6                        mov r8d, esi
00816920  48 8B CF                        mov rcx, rdi
00816923  E8 9C FD FF FF                  call 0x1408166c4
00816928  85 C0                           test eax, eax
0081692A  74 2C                           je 0x140816958
0081692C  41 8B 56 2C                     mov edx, dword ptr [r14 + 0x2c]
00816930  66 41 B9 34 40                  mov r9w, 0x4034
00816935  66 C7 44 24 28 36 40            mov word ptr [rsp + 0x28], 0x4036
0081693C  44 8B C6                        mov r8d, esi
0081693F  48 8B CF                        mov rcx, rdi
00816942  66 C7 44 24 20 35 40            mov word ptr [rsp + 0x20], 0x4035
00816949  E8 EA FC FF FF                  call 0x140816638
0081694E  85 C0                           test eax, eax
00816950  B9 01 00 00 00                  mov ecx, 1
00816955  0F 45 D9                        cmovne ebx, ecx
00816958  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
0081695D  8B C3                           mov eax, ebx
0081695F  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00816964  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00816969  48 83 C4 30                     add rsp, 0x30
0081696D  41 5E                           pop r14
0081696F  C3                              ret
00816970  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SdbpMatchOem(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int16 v_stack_m10;
    unsigned __int16 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (48);
    v_rbx = 0;
    result = SdbFindFirstTag(a1, a2, (unsigned int)(0x7022ULL), a4);
    if ((unsigned int)(result) != 0) goto loc_008168FB;
    goto loc_00816958;
loc_008168FB:
    result = SdbpMatchDeviceString(a1, *(unsigned __int64 *)(a3), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(0x6025ULL));
    if ((unsigned int)(result) == 0) goto loc_00816958;
    result = SdbpMatchDeviceString(a1, *(unsigned __int64 *)(a3 + 8), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(0x6026ULL));
    v_rbx = result + 1;
    if ((unsigned int)(result) != 0) {
        a2 = *(unsigned int *)(a3 + 44);
        a4 = 0x4034ULL;
        v_stack_m10 = 0x4036ULL;
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a1 = a1;
        v_stack_m18 = 0x4035ULL;
        result = SdbpMatchDeviceDWORD(a1, a2, a3, a4);
        a1 = 1;
        v_rbx = result + 1;
        if ((unsigned int)(result) != 0) { v_rbx = (unsigned int)(a1); }
    }
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t SdbpMatchOem(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint16_t v_stack_m10;
    uint16_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (48);
    local_rbx = 0;
    result = SdbFindFirstTag(Arg1, Arg2, (uint32_t)(0x7022ULL), a4);
    if ((uint32_t)(result) != 0) goto loc_008168FB;
    goto loc_00816958;
loc_008168FB:
    result = SdbpMatchDeviceString(Arg1, *(uint64_t *)(arg3), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(0x6025ULL));
    if ((uint32_t)(result) == 0) goto loc_00816958;
    result = SdbpMatchDeviceString(Arg1, *(uint64_t *)(arg3 + 0x8), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(0x6026ULL));
    local_rbx = result + 1;
    if ((uint32_t)(result) != 0) {
        Arg2 = *(uint32_t *)(arg3 + 0x2C);
        a4 = 0x4034ULL;
        v_stack_m10 = 0x4036ULL;
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg1 = Arg1;
        v_stack_m18 = 0x4035ULL;
        result = SdbpMatchDeviceDWORD(Arg1, Arg2, Arg3, a4);
        Arg1 = 1;
        local_rbx = result + 1;
        if ((uint32_t)(result) != 0) { local_rbx = (uint32_t)(Arg1); }
    }
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x2C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008168C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008168C8[BB_008168C8]
  bb_008168F6[BB_008168F6]
  bb_008168FB[BB_008168FB]
  bb_00816913[BB_00816913]
  bb_0081692C[BB_0081692C]
  bb_00816958[BB_00816958]
  bb_00816970[BB_00816970]
  bb_008168C8 -->|branch| bb_008168FB
  bb_008168C8 -->|fallthrough| bb_008168F6
  bb_008168F6 -->|branch| bb_00816958
  bb_008168FB -->|branch| bb_00816958
  bb_008168FB -->|fallthrough| bb_00816913
  bb_00816913 -->|branch| bb_00816958
  bb_00816913 -->|fallthrough| bb_0081692C
  bb_0081692C -->|flow| bb_00816958
```
