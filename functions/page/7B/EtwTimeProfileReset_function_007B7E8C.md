# EtwTimeProfileReset

- RVA: `0x007B7E8C`–`0x007B7EB1` (길이 `37` bytes)
- VA: `0x00000001407B7E8C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007B7EA1` → [KeStopProfile](../../text/5C/KeStopProfile_function_005C0640.md) (function, `0x005C0640`)
- `0x007B7EA6` → [EtwpTimeProfileStart](../6F/EtwpTimeProfileStart_function_006FF5E0.md) (function, `0x006FF5E0`)

### Direct callers
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D05A`

### Static image references
- `0x007B7E90` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x007B7E9A` → RVA `0x00EFF520` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007B7EA1` → [KeStopProfile](../../text/5C/KeStopProfile_function_005C0640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B7E8C  48 83 EC 28                     sub rsp, 0x28
007B7E90  8B 05 6E EC 80 00               mov eax, dword ptr [rip + 0x80ec6e]
007B7E96  A8 02                           test al, 2
007B7E98  74 11                           je 0x1407b7eab
007B7E9A  48 8D 0D 7F 76 74 00            lea rcx, [rip + 0x74767f]
007B7EA1  E8 9A 87 E0 FF                  call 0x1405c0640
007B7EA6  E8 35 77 F4 FF                  call 0x1406ff5e0
007B7EAB  48 83 C4 28                     add rsp, 0x28
007B7EAF  C3                              ret
007B7EB0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTimeProfileReset(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(*(unsigned int *)(v_rip + 8449134));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 8449134)))) & (2)) != 0) {
        a1 = v_rip + 7632511;
        result = KeStopProfile(a1, a2, a3, a4);
        result = EtwpTimeProfileStart(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void EtwTimeProfileReset(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x80EC6E));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x80EC6E)))) & (2)) != 0) {
        a1 = v_rip + 7632511;
        result = KeStopProfile(a1, a2, a3, a4);
        result = EtwpTimeProfileStart(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B7E8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007B7E8C[BB_007B7E8C]
  bb_007B7E9A[BB_007B7E9A]
  bb_007B7EAB[BB_007B7EAB]
  bb_007B7EB0[BB_007B7EB0]
  bb_007B7E8C -->|branch| bb_007B7EAB
  bb_007B7E8C -->|fallthrough| bb_007B7E9A
  bb_007B7E9A -->|flow| bb_007B7EAB
```
