# PiPnpRtlOperationListAcquireExclusiveLock

- RVA: `0x008E065C`–`0x008E0685` (길이 `41` bytes)
- VA: `0x00000001408E065C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008E067A` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)

### Direct callers
- [PiPnpRtlBeginOperation](PiPnpRtlBeginOperation_function_008E033C.md) at `0x008E03EA`
- [PiPnpRtlEndOperation](PiPnpRtlEndOperation_function_008E0518.md) at `0x008E0539`

### Static image references
- `0x008E0669` → RVA `0x00F8B9E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008E067A` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008E065C  48 83 EC 28                     sub rsp, 0x28
008E0660  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008E0669  48 8D 0D 70 B3 6A 00            lea rcx, [rip + 0x6ab370]
008E0670  B2 01                           mov dl, 1
008E0672  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008E0679  90                              nop
008E067A  E8 A1 47 93 FF                  call 0x140214e20
008E067F  48 83 C4 28                     add rsp, 0x28
008E0683  C3                              ret
008E0684  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiPnpRtlOperationListAcquireExclusiveLock(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAcquireResourceExclusiveLite(v_rip + 6992752, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PiPnpRtlOperationListAcquireExclusiveLock(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAcquireResourceExclusiveLite(v_rip + 6992752, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E065C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008E065C[BB_008E065C]
  bb_008E0684[BB_008E0684]
```
