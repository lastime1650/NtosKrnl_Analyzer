# MmGetMaximumNonPagedPoolInBytes

- RVA: `0x004BA168`–`0x004BA175` (길이 `13` bytes)
- VA: `0x00000001404BA168`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `13/13` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EtwpGetSystemMaximumBufferCount](../../page/A7/EtwpGetSystemMaximumBufferCount_function_00A74890.md) at `0x00A748B0`
- [ExEnableHandleTracing](../../page/AD/ExEnableHandleTracing_function_00AD2C8C.md) at `0x00AD2D25`

### Static image references
- `0x004BA168` → RVA `0x00E37658` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BA168  48 8B 05 E9 D4 97 00            mov rax, qword ptr [rip + 0x97d4e9]
004BA16F  48 C1 E0 0C                     shl rax, 0xc
004BA173  C3                              ret
004BA174  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmGetMaximumNonPagedPoolInBytes(void)
{
    __int64 result;

    result = (*(unsigned __int64 *)(v_rip + 9950441)) << (12);
    return result;
}
```

## 5. (Beta) C Style

```c
void MmGetMaximumNonPagedPoolInBytes(void)
{
    int64_t result;

    result = (*(uint64_t *)(v_rip + 0x97D4E9)) << (12);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BA168&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BA168[BB_004BA168]
  bb_004BA174[BB_004BA174]
```
