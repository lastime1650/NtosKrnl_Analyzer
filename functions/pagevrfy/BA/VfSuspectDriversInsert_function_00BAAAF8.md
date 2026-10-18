# VfSuspectDriversInsert

- RVA: `0x00BAAAF8`–`0x00BAAB25` (길이 `45` bytes)
- VA: `0x0000000140BAAAF8`
- 실행 섹션: `PAGEVRFY`
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
- [VfSuspectDriversParseRegistryString](../../init/C4/VfSuspectDriversParseRegistryString_function_00C4C820.md) at `0x00C4C952`

### Static image references
- `0x00BAAAF8` → RVA `0x00F049E8` (`.data`; read)
- `0x00BAAAFF` → RVA `0x00F049E0` (`.data`; read)
- `0x00BAAB1C` → RVA `0x00F049E8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAAAF8  48 8B 05 E9 9E 35 00            mov rax, qword ptr [rip + 0x359ee9]
00BAAAFF  48 8D 15 DA 9E 35 00            lea rdx, [rip + 0x359eda]
00BAAB06  48 39 10                        cmp qword ptr [rax], rdx
00BAAB09  74 07                           je 0x140baab12
00BAAB0B  B9 03 00 00 00                  mov ecx, 3
00BAAB10  CD 29                           int 0x29
00BAAB12  48 89 11                        mov qword ptr [rcx], rdx
00BAAB15  48 89 41 08                     mov qword ptr [rcx + 8], rax
00BAAB19  48 89 08                        mov qword ptr [rax], rcx
00BAAB1C  48 89 0D C5 9E 35 00            mov qword ptr [rip + 0x359ec5], rcx
00BAAB23  C3                              ret
00BAAB24  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfSuspectDriversInsert(void)
{
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3514089))) != (v_rip + 3514074)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a1) = v_rip + 3514074;
    *(unsigned __int64 *)(a1 + 8) = *(unsigned __int64 *)(v_rip + 3514089);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 3514089)) = a1;
    *(unsigned __int64 *)(v_rip + 3514053) = a1;
    return *(unsigned __int64 *)(v_rip + 3514089);
}
```

## 5. (Beta) C Style

```c
void VfSuspectDriversInsert(void)
{
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x359EE9))) != (v_rip + 3514074)) {
        a1 = 3;
    }
    *(uint64_t *)(a1) = v_rip + 3514074;
    *(uint64_t *)(a1 + 0x8) = *(uint64_t *)(v_rip + 0x359EE9);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x359EE9)) = a1;
    *(uint64_t *)(v_rip + 0x359EC5) = a1;
    return *(uint64_t *)(v_rip + 0x359EE9);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAAAF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAAAF8[BB_00BAAAF8]
  bb_00BAAB0B[BB_00BAAB0B]
  bb_00BAAB12[BB_00BAAB12]
  bb_00BAAB24[BB_00BAAB24]
  bb_00BAAAF8 -->|branch| bb_00BAAB12
  bb_00BAAAF8 -->|fallthrough| bb_00BAAB0B
  bb_00BAAB0B -->|flow| bb_00BAAB12
```
