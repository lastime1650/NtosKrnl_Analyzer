# ExTryConvertSharedToExclusiveLite

- RVA: `0x00658DDC`–`0x00658E13` (길이 `55` bytes)
- VA: `0x0000000140658DDC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `15`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00658E02` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00658E08` → [ExpTryConvertSharedToExclusiveLite](ExpTryConvertSharedToExclusiveLite_function_00658F30.md) (function, `0x00658F30`)

### Direct callers
- [CmpReplicateKeyToVirtual](../../page/7E/CmpReplicateKeyToVirtual_function_007EBAEC.md) at `0x007EBB8A`

### Static image references
- `0x00658DE0` → RVA `0x00EF7110` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00658DDC  48 83 EC 38                     sub rsp, 0x38
00658DE0  48 8B 0D 29 E3 89 00            mov rcx, qword ptr [rip + 0x89e329]
00658DE7  F6 41 1A 01                     test byte ptr [rcx + 0x1a], 1
00658DEB  74 1B                           je 0x140658e08
00658DED  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00658DF3  45 33 C9                        xor r9d, r9d
00658DF6  4C 8B C1                        mov r8, rcx
00658DF9  B9 C6 01 00 00                  mov ecx, 0x1c6
00658DFE  41 8D 51 0E                     lea edx, [r9 + 0xe]
00658E02  E8 59 48 EA FF                  call 0x1404fd660
00658E07  CC                              int3
00658E08  E8 23 01 00 00                  call 0x140658f30
00658E0D  48 83 C4 38                     add rsp, 0x38
00658E11  C3                              ret
00658E12  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExTryConvertSharedToExclusiveLite(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 9036585) + 26)) & (1)) != 0) {
        a4 = 0;
        a3 = *(unsigned __int64 *)(v_rip + 9036585);
        a1 = 454;
        a2 = a4 + 14;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = ExpTryConvertSharedToExclusiveLite(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExTryConvertSharedToExclusiveLite(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x89E329) + 0x1A)) & (1)) != 0) {
        Arg4 = 0;
        Arg3 = *(uint64_t *)(v_rip + 0x89E329);
        Arg1 = 454;
        Arg2 = Arg4 + 14;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExpTryConvertSharedToExclusiveLite(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00658DDC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00658DDC[BB_00658DDC]
  bb_00658DED[BB_00658DED]
  bb_00658E08[BB_00658E08]
  bb_00658E12[BB_00658E12]
  bb_00658DDC -->|branch| bb_00658E08
  bb_00658DDC -->|fallthrough| bb_00658DED
  bb_00658DED -->|flow| bb_00658E08
```
