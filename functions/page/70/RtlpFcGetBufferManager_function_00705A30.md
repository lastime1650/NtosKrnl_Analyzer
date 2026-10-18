# RtlpFcGetBufferManager

- RVA: `0x00705A30`–`0x00705A39` (길이 `9` bytes)
- VA: `0x0000000140705A30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `9/9` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlQueryFeatureConfiguration](../../text/4B/RtlQueryFeatureConfiguration_function_004BDD10.md) at `0x004BDD64`
- [RtlQueryAllInternalFeatureConfigurations](../../text/5E/RtlQueryAllInternalFeatureConfigurations_function_005E7280.md) at `0x005E72AE`
- [RtlQueryAllInternalRuntimeFeatureConfigurations](../../text/5E/RtlQueryAllInternalRuntimeFeatureConfigurations_function_005E7320.md) at `0x005E7353`
- [RtlQueryInternalFeatureConfiguration](../../text/5E/RtlQueryInternalFeatureConfiguration_function_005E7500.md) at `0x005E7551`

### Static image references
- `0x00705A30` → RVA `0x00EF7368` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00705A30  48 8D 05 31 19 7F 00            lea rax, [rip + 0x7f1931]
00705A37  C3                              ret
00705A38  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpFcGetBufferManager(void)
{
    return v_rip + 8329521;
}
```

## 5. (Beta) C Style

```c
void RtlpFcGetBufferManager(void)
{
    return v_rip + 8329521;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00705A30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00705A30[BB_00705A30]
  bb_00705A38[BB_00705A38]
```
