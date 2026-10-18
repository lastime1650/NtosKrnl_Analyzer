# CmpValidateGlobalFlushControlFlags

- RVA: `0x007E7F50`–`0x007E7F65` (길이 `21` bytes)
- VA: `0x00000001407E7F50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmInitSystem1](../../init/C5/CmInitSystem1_function_00C559CC.md) at `0x00C55C5E`

### Static image references
- `0x007E7F50` → RVA `0x00EF7230` (`.data`; read)
- `0x007E7F5C` → RVA `0x00EF7230` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E7F50  F7 05 D6 F2 70 00 FE FF FF FF   test dword ptr [rip + 0x70f2d6], 0xfffffffe
007E7F5A  74 07                           je 0x1407e7f63
007E7F5C  83 25 CD F2 70 00 00            and dword ptr [rip + 0x70f2cd], 0
007E7F63  C3                              ret
007E7F64  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall CmpValidateGlobalFlushControlFlags(void)
{
    if (((*(unsigned int *)(v_rip + 7402198)) & (0xFFFFFFFEULL)) != 0) {
    }
    return;
}
```

## 5. (Beta) C Style

```c
void CmpValidateGlobalFlushControlFlags(void)
{
    if (((*(uint32_t *)(v_rip + 0x70F2D6)) & (0xFFFFFFFEULL)) != 0) {
    }
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E7F50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E7F50[BB_007E7F50]
  bb_007E7F5C[BB_007E7F5C]
  bb_007E7F63[BB_007E7F63]
  bb_007E7F64[BB_007E7F64]
  bb_007E7F50 -->|branch| bb_007E7F63
  bb_007E7F50 -->|fallthrough| bb_007E7F5C
  bb_007E7F5C -->|flow| bb_007E7F63
```
