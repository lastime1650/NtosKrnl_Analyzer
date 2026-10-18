# CmpLockHiveListShared

- RVA: `0x0084E3C8`–`0x0084E41C` (길이 `84` bytes)
- VA: `0x000000014084E3C8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0084E3DA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0084E407` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [CmpVEExecuteRealStoreParseLogic](CmpVEExecuteRealStoreParseLogic_function_0084CCD4.md) at `0x0084CD44`
- [CmpBlockHiveWrites](CmpBlockHiveWrites_function_0084CF94.md) at `0x0084CFB2`
- [CmpGetNextActiveHive](CmpGetNextActiveHive_function_0084E2A0.md) at `0x0084E2C8`
- [CmpGetNextHive](CmpGetNextHive_function_0084E330.md) at `0x0084E35F`
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x0085FB7B`
- [CmpGetLastHive](../87/CmpGetLastHive_function_008786B4.md) at `0x008786BC`

### Static image references
- `0x0084E3D1` → RVA `0x00EF7C70` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0084E3DA` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0084E407` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0084E3C8  40 53                           push rbx
0084E3CA  48 83 EC 20                     sub rsp, 0x20
0084E3CE  45 33 C0                        xor r8d, r8d
0084E3D1  48 8D 0D 98 98 6A 00            lea rcx, [rip + 0x6a9898]
0084E3D8  33 D2                           xor edx, edx
0084E3DA  E8 51 1E 9C FF                  call 0x140210230
0084E3DF  48 8B D8                        mov rbx, rax
0084E3E2  BA 11 00 00 00                  mov edx, 0x11
0084E3E7  33 C0                           xor eax, eax
0084E3E9  F0 48 0F B1 15 7E 98 6A 00      lock cmpxchg qword ptr [rip + 0x6a987e], rdx
0084E3F2  74 18                           je 0x14084e40c
0084E3F4  4C 8D 0D 75 98 6A 00            lea r9, [rip + 0x6a9875]
0084E3FB  4C 8B C3                        mov r8, rbx
0084E3FE  33 D2                           xor edx, edx
0084E400  48 8D 0D 69 98 6A 00            lea rcx, [rip + 0x6a9869]
0084E407  E8 40 20 9C FF                  call 0x14021044c
0084E40C  48 85 DB                        test rbx, rbx
0084E40F  74 04                           je 0x14084e415
0084E411  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0084E415  48 83 C4 20                     add rsp, 0x20
0084E419  5B                              pop rbx
0084E41A  C3                              ret
0084E41B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLockHiveListShared(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6985880, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6985845;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 6985833;
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
int64_t CmpLockHiveListShared(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6985880, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6985845;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 6985833;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084E3C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0084E3C8[BB_0084E3C8]
  bb_0084E3F4[BB_0084E3F4]
  bb_0084E40C[BB_0084E40C]
  bb_0084E411[BB_0084E411]
  bb_0084E415[BB_0084E415]
  bb_0084E41B[BB_0084E41B]
  bb_0084E3C8 -->|branch| bb_0084E40C
  bb_0084E3C8 -->|fallthrough| bb_0084E3F4
  bb_0084E3F4 -->|flow| bb_0084E40C
  bb_0084E40C -->|branch| bb_0084E415
  bb_0084E40C -->|fallthrough| bb_0084E411
  bb_0084E411 -->|flow| bb_0084E415
```
