# CmpLockCallbackListShared

- RVA: `0x0099E9B0`–`0x0099EA15` (길이 `101` bytes)
- VA: `0x000000014099E9B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `26`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0099E9D3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0099EA00` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [CmpEnumerateCallback](../7E/CmpEnumerateCallback_function_007E18D0.md) at `0x007E18FA`

### Static image references
- `0x0099E9BF` → RVA `0x00EF7BD0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0099E9D3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0099EA00` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0099E9B0  40 53                           push rbx
0099E9B2  48 83 EC 20                     sub rsp, 0x20
0099E9B6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0099E9BF  48 8D 0D 0A 92 55 00            lea rcx, [rip + 0x55920a]
0099E9C6  45 33 C0                        xor r8d, r8d
0099E9C9  33 D2                           xor edx, edx
0099E9CB  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0099E9D2  90                              nop
0099E9D3  E8 58 18 87 FF                  call 0x140210230
0099E9D8  48 8B D8                        mov rbx, rax
0099E9DB  BA 11 00 00 00                  mov edx, 0x11
0099E9E0  33 C0                           xor eax, eax
0099E9E2  F0 48 0F B1 15 E5 91 55 00      lock cmpxchg qword ptr [rip + 0x5591e5], rdx
0099E9EB  74 18                           je 0x14099ea05
0099E9ED  4C 8D 0D DC 91 55 00            lea r9, [rip + 0x5591dc]
0099E9F4  4C 8B C3                        mov r8, rbx
0099E9F7  33 D2                           xor edx, edx
0099E9F9  48 8D 0D D0 91 55 00            lea rcx, [rip + 0x5591d0]
0099EA00  E8 47 1A 87 FF                  call 0x14021044c
0099EA05  48 85 DB                        test rbx, rbx
0099EA08  74 04                           je 0x14099ea0e
0099EA0A  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0099EA0E  48 83 C4 20                     add rsp, 0x20
0099EA12  5B                              pop rbx
0099EA13  C3                              ret
0099EA14  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLockCallbackListShared(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 5607946, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 5607900;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 5607888;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpLockCallbackListShared(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 5607946, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 5607900;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 5607888;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0099E9B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0099E9B0[BB_0099E9B0]
  bb_0099E9ED[BB_0099E9ED]
  bb_0099EA05[BB_0099EA05]
  bb_0099EA0A[BB_0099EA0A]
  bb_0099EA0E[BB_0099EA0E]
  bb_0099EA14[BB_0099EA14]
  bb_0099E9B0 -->|branch| bb_0099EA05
  bb_0099E9B0 -->|fallthrough| bb_0099E9ED
  bb_0099E9ED -->|flow| bb_0099EA05
  bb_0099EA05 -->|branch| bb_0099EA0E
  bb_0099EA05 -->|fallthrough| bb_0099EA0A
  bb_0099EA0A -->|flow| bb_0099EA0E
```
