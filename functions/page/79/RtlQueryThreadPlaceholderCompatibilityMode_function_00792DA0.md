# RtlQueryThreadPlaceholderCompatibilityMode

- RVA: `0x00792DA0`–`0x00792DD3` (길이 `51` bytes)
- VA: `0x0000000140792DA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00792DA0  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00792DA9  F7 41 74 00 04 00 00            test dword ptr [rcx + 0x74], 0x400
00792DB0  75 1D                           jne 0x140792dcf
00792DB2  80 B9 4A 02 00 00 01            cmp byte ptr [rcx + 0x24a], 1
00792DB9  74 14                           je 0x140792dcf
00792DBB  48 8B 81 F0 00 00 00            mov rax, qword ptr [rcx + 0xf0]
00792DC2  48 85 C0                        test rax, rax
00792DC5  74 08                           je 0x140792dcf
00792DC7  8A 80 80 02 00 00               mov al, byte ptr [rax + 0x280]
00792DCD  C3                              ret
00792DCE  CC                              int3
00792DCF  B0 FE                           mov al, 0xfe
00792DD1  C3                              ret
00792DD2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlQueryThreadPlaceholderCompatibilityMode(void)
{
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x400ULL)) != 0) goto loc_00792DCF;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)) == 1) goto loc_00792DCF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) == 0) goto loc_00792DCF;
    return *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 240) + 640);
loc_00792DCF:
    return 254;
}
```

## 5. (Beta) C Style

```c
void RtlQueryThreadPlaceholderCompatibilityMode(void)
{
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x400ULL)) != 0) goto loc_00792DCF;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)) == 1) goto loc_00792DCF;
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) == 0) goto loc_00792DCF;
    return *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xF0) + 0x280);
loc_00792DCF:
    return 254;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00792DA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00792DA0[BB_00792DA0]
  bb_00792DB2[BB_00792DB2]
  bb_00792DBB[BB_00792DBB]
  bb_00792DC7[BB_00792DC7]
  bb_00792DCE[BB_00792DCE]
  bb_00792DCF[BB_00792DCF]
  bb_00792DD2[BB_00792DD2]
  bb_00792DA0 -->|branch| bb_00792DCF
  bb_00792DA0 -->|fallthrough| bb_00792DB2
  bb_00792DB2 -->|branch| bb_00792DCF
  bb_00792DB2 -->|fallthrough| bb_00792DBB
  bb_00792DBB -->|branch| bb_00792DCF
  bb_00792DBB -->|fallthrough| bb_00792DC7
  bb_00792DCE -->|flow| bb_00792DCF
```
