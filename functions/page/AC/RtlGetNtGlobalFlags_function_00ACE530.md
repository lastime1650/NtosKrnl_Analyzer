# RtlGetNtGlobalFlags

- RVA: `0x00ACE530`–`0x00ACE538` (길이 `8` bytes)
- VA: `0x0000000140ACE530`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `8/8` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlpCreateHeap](../../text/4E/RtlpCreateHeap_function_004E1904.md) at `0x004E1965`
- [RtlpCreateHeap](../../text/4E/RtlpCreateHeap_function_004E1904.md) at `0x004E20EE`
- [RtlpAllocateHeap](../../text/5E/RtlpAllocateHeap_function_005E8B1C.md) at `0x005E8C8D`

### Static image references
- `0x00ACE530` → RVA `0x00FC42C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ACE530  8B 05 8A 5D 4F 00               mov eax, dword ptr [rip + 0x4f5d8a]
00ACE536  C3                              ret
00ACE537  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlGetNtGlobalFlags(void)
{
    return (unsigned int)(*(unsigned int *)(v_rip + 5201290));
}
```

## 5. (Beta) C Style

```c
void RtlGetNtGlobalFlags(void)
{
    return (uint32_t)(*(uint32_t *)(v_rip + 0x4F5D8A));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ACE530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ACE530[BB_00ACE530]
  bb_00ACE537[BB_00ACE537]
```
