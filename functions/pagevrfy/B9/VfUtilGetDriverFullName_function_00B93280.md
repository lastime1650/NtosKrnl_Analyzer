# VfUtilGetDriverFullName

- RVA: `0x00B93280`–`0x00B9329B` (길이 `27` bytes)
- VA: `0x0000000140B93280`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B93284` → [VfTargetDriversGetVerifierData](../BB/VfTargetDriversGetVerifierData_function_00BB7E6C.md) (function, `0x00BB7E6C`)

### Direct callers
- [CarEtwWriteBugCheckEvent](../../text/61/CarEtwWriteBugCheckEvent_function_00617B68.md) at `0x00617B98`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B93280  48 83 EC 28                     sub rsp, 0x28
00B93284  E8 E3 4B 02 00                  call 0x140bb7e6c
00B93289  48 85 C0                        test rax, rax
00B9328C  74 07                           je 0x140b93295
00B9328E  48 8B 00                        mov rax, qword ptr [rax]
00B93291  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
00B93295  48 83 C4 28                     add rsp, 0x28
00B93299  C3                              ret
00B9329A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfUtilGetDriverFullName(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = VfTargetDriversGetVerifierData(a1, a2, a3, a4);
    if (result != 0) {
        result = *(unsigned __int64 *)(result);
        result = *(unsigned __int64 *)(result + 32);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void VfUtilGetDriverFullName(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = VfTargetDriversGetVerifierData(a1, a2, a3, a4);
    if (result != 0) {
        result = *(uint64_t *)(result);
        result = *(uint64_t *)(result + 0x20);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B93280&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B93280[BB_00B93280]
  bb_00B9328E[BB_00B9328E]
  bb_00B93295[BB_00B93295]
  bb_00B9329A[BB_00B9329A]
  bb_00B93280 -->|branch| bb_00B93295
  bb_00B93280 -->|fallthrough| bb_00B9328E
  bb_00B9328E -->|flow| bb_00B93295
```
