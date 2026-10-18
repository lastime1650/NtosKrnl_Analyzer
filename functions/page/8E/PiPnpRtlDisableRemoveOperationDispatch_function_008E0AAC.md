# PiPnpRtlDisableRemoveOperationDispatch

- RVA: `0x008E0AAC`–`0x008E0AD5` (길이 `41` bytes)
- VA: `0x00000001408E0AAC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008E0ACA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)

### Direct callers
- [PiPnpRtlEnsureObjectCached](../72/PiPnpRtlEnsureObjectCached_function_0072F928.md) at `0x0072F9C3`
- [PiPnpRtlEndOperation](PiPnpRtlEndOperation_function_008E0518.md) at `0x008E0534`
- [sub_008E078C](Unknown_function_008E078C.md) at `0x008E0794`
- [PiPnpRtlObjectEventWorker](../8F/PiPnpRtlObjectEventWorker_function_008F8630.md) at `0x008F86A1`
- [PiPnpRtlObjectEventWorker](../8F/PiPnpRtlObjectEventWorker_function_008F8630.md) at `0x008F8729`
- [sub_00B1F154](../B1/Unknown_function_00B1F154.md) at `0x00B1F1B3`

### Static image references
- `0x008E0AB9` → RVA `0x00F8B960` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008E0ACA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008E0AAC  48 83 EC 28                     sub rsp, 0x28
008E0AB0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008E0AB9  48 8D 0D A0 AE 6A 00            lea rcx, [rip + 0x6aaea0]
008E0AC0  B2 01                           mov dl, 1
008E0AC2  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008E0AC9  90                              nop
008E0ACA  E8 F1 10 93 FF                  call 0x140211bc0
008E0ACF  48 83 C4 28                     add rsp, 0x28
008E0AD3  C3                              ret
008E0AD4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiPnpRtlDisableRemoveOperationDispatch(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAcquireResourceSharedLite(v_rip + 6991520, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PiPnpRtlDisableRemoveOperationDispatch(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAcquireResourceSharedLite(v_rip + 6991520, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E0AAC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008E0AAC[BB_008E0AAC]
  bb_008E0AD4[BB_008E0AD4]
```
