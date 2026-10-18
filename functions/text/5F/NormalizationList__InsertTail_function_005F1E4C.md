# NormalizationList__InsertTail

- RVA: `0x005F1E4C`–`0x005F1E79` (길이 `45` bytes)
- VA: `0x00000001405F1E4C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlpGetNormalization](../../page/79/RtlpGetNormalization_function_0079AB58.md) at `0x0079AC35`

### Static image references
- `0x005F1E4C` → RVA `0x00E08860` (`.data`; read)
- `0x005F1E53` → RVA `0x00E08858` (`.data`; read)
- `0x005F1E70` → RVA `0x00E08860` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005F1E4C  48 8B 05 0D 6A 81 00            mov rax, qword ptr [rip + 0x816a0d]
005F1E53  48 8D 15 FE 69 81 00            lea rdx, [rip + 0x8169fe]
005F1E5A  48 39 10                        cmp qword ptr [rax], rdx
005F1E5D  74 07                           je 0x1405f1e66
005F1E5F  B9 03 00 00 00                  mov ecx, 3
005F1E64  CD 29                           int 0x29
005F1E66  48 89 11                        mov qword ptr [rcx], rdx
005F1E69  48 89 41 08                     mov qword ptr [rcx + 8], rax
005F1E6D  48 89 08                        mov qword ptr [rax], rcx
005F1E70  48 89 0D E9 69 81 00            mov qword ptr [rip + 0x8169e9], rcx
005F1E77  C3                              ret
005F1E78  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NormalizationList__InsertTail(void)
{
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8481293))) != (v_rip + 8481278)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a1) = v_rip + 8481278;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(v_rip + 8481293);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8481293)) = a1;
    *(unsigned __int64 *)(v_rip + 8481257) = a1;
    return *(unsigned __int64 *)(v_rip + 8481293);
}
```

## 5. (Beta) C Style

```c
void NormalizationList__InsertTail(void)
{
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x816A0D))) != (v_rip + 8481278)) {
        a1 = 3;
    }
    *(uint64_t *)(a1) = v_rip + 8481278;
    *(uint64_t *)(a1 + 0x8) = *(uint64_t *)(v_rip + 0x816A0D);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x816A0D)) = a1;
    *(uint64_t *)(v_rip + 0x8169E9) = a1;
    return *(uint64_t *)(v_rip + 0x816A0D);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005F1E4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005F1E4C[BB_005F1E4C]
  bb_005F1E5F[BB_005F1E5F]
  bb_005F1E66[BB_005F1E66]
  bb_005F1E78[BB_005F1E78]
  bb_005F1E4C -->|branch| bb_005F1E66
  bb_005F1E4C -->|fallthrough| bb_005F1E5F
  bb_005F1E5F -->|flow| bb_005F1E66
```
