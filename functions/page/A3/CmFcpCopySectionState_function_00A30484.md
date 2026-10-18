# CmFcpCopySectionState

- RVA: `0x00A30484`–`0x00A304AC` (길이 `40` bytes)
- VA: `0x0000000140A30484`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A304A1` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)

### Direct callers
- [CmFcManagerQueryFeatureConfigurationSectionInformation](CmFcManagerQueryFeatureConfigurationSectionInformation_function_00A30240.md) at `0x00A30322`
- [CmFcManagerStartRuntimePhase](../../init/C5/CmFcManagerStartRuntimePhase_function_00C5DC70.md) at `0x00C5DD95`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A304A1` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A30484  48 83 EC 28                     sub rsp, 0x28
00A30488  0F 10 02                        movups xmm0, xmmword ptr [rdx]
00A3048B  0F 11 01                        movups xmmword ptr [rcx], xmm0
00A3048E  F2 0F 10 4A 10                  movsd xmm1, qword ptr [rdx + 0x10]
00A30493  F2 0F 11 49 10                  movsd qword ptr [rcx + 0x10], xmm1
00A30498  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
00A3049C  48 85 C9                        test rcx, rcx
00A3049F  74 05                           je 0x140a304a6
00A304A1  E8 7A F5 7D FF                  call 0x14020fa20
00A304A6  48 83 C4 28                     add rsp, 0x28
00A304AA  C3                              ret
00A304AB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmFcpCopySectionState(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm1;
    if (*(unsigned __int64 *)(a1 + 8) != 0) {
        result = ObfReferenceObject(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmFcpCopySectionState(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint64_t *)(arg1) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10) = v_xmm1;
    if (*(uint64_t *)(arg1 + 0x8) != 0) {
        result = ObfReferenceObject(*(uint64_t *)(arg1 + 0x8), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A30484&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A30484[BB_00A30484]
  bb_00A304A1[BB_00A304A1]
  bb_00A304A6[BB_00A304A6]
  bb_00A304AB[BB_00A304AB]
  bb_00A30484 -->|branch| bb_00A304A6
  bb_00A30484 -->|fallthrough| bb_00A304A1
  bb_00A304A1 -->|flow| bb_00A304A6
```
