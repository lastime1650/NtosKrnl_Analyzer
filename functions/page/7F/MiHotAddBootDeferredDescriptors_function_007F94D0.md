# MiHotAddBootDeferredDescriptors

- RVA: `0x007F94D0`–`0x007F94F0` (길이 `32` bytes)
- VA: `0x00000001407F94D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007F94D4` → [MiHotAddBootDeferredDescriptorsDiscardable](../../init/C6/MiHotAddBootDeferredDescriptorsDiscardable_function_00C624E4.md) (function, `0x00C624E4`)
- `0x007F94E5` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007F94DC` → RVA `0x00E2FFA8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007F94D4` → [MiHotAddBootDeferredDescriptorsDiscardable](../../init/C6/MiHotAddBootDeferredDescriptorsDiscardable_function_00C624E4.md) (`PAGE` → `INIT`)
  - `0x007F94E5` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F94D0  48 83 EC 28                     sub rsp, 0x28
007F94D4  E8 0B 90 46 00                  call 0x140c624e4
007F94D9  45 33 C0                        xor r8d, r8d
007F94DC  48 8D 0D C5 6A 63 00            lea rcx, [rip + 0x636ac5]
007F94E3  33 D2                           xor edx, edx
007F94E5  E8 26 5E B4 FF                  call 0x14033f310
007F94EA  48 83 C4 28                     add rsp, 0x28
007F94EE  C3                              ret
007F94EF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiHotAddBootDeferredDescriptors(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiHotAddBootDeferredDescriptorsDiscardable(a1, a2, a3, a4);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 6515397, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiHotAddBootDeferredDescriptors(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiHotAddBootDeferredDescriptorsDiscardable(Arg1, Arg2, Arg3, a4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 6515397, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F94D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007F94D0[BB_007F94D0]
  bb_007F94EF[BB_007F94EF]
```
