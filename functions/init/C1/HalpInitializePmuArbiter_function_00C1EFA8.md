# HalpInitializePmuArbiter

- RVA: `0x00C1EFA8`–`0x00C1EFDB` (길이 `51` bytes)
- VA: `0x0000000140C1EFA8`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpHwPerfCntInitSystem](../../pagelk/B5/HalpHwPerfCntInitSystem_function_00B5C590.md) at `0x00B5C666`

### Static image references
- `0x00C1EFA8` → RVA `0x00FC2B40` (`.data`; read/write)
- `0x00C1EFB0` → RVA `0x00FC2B58` (`.data`; read)
- `0x00C1EFB7` → RVA `0x00FC2B60` (`.data`; write)
- `0x00C1EFBE` → RVA `0x00FC2B58` (`.data`; write)
- `0x00C1EFC5` → RVA `0x00FC2BC0` (`.data`; write)
- `0x00C1EFCF` → RVA `0x00FC2B50` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C1EFA8  48 83 25 90 3B 3A 00 00         and qword ptr [rip + 0x3a3b90], 0
00C1EFB0  48 8D 05 A1 3B 3A 00            lea rax, [rip + 0x3a3ba1]
00C1EFB7  48 89 05 A2 3B 3A 00            mov qword ptr [rip + 0x3a3ba2], rax
00C1EFBE  48 89 05 93 3B 3A 00            mov qword ptr [rip + 0x3a3b93], rax
00C1EFC5  C7 05 F1 3B 3A 00 E0 93 04 00   mov dword ptr [rip + 0x3a3bf1], 0x493e0
00C1EFCF  C7 05 77 3B 3A 00 01 00 00 00   mov dword ptr [rip + 0x3a3b77], 1
00C1EFD9  C3                              ret
00C1EFDA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpInitializePmuArbiter(void)
{
    *(unsigned __int64 *)(v_rip + 3816354) = v_rip + 3816353;
    *(unsigned __int64 *)(v_rip + 3816339) = v_rip + 3816353;
    *(unsigned int *)(v_rip + 3816433) = 0x493E0ULL;
    *(unsigned int *)(v_rip + 3816311) = 1;
    return v_rip + 3816353;
}
```

## 5. (Beta) C Style

```c
void HalpInitializePmuArbiter(void)
{
    *(uint64_t *)(v_rip + 0x3A3BA2) = v_rip + 3816353;
    *(uint64_t *)(v_rip + 0x3A3B93) = v_rip + 3816353;
    *(uint32_t *)(v_rip + 0x3A3BF1) = 0x493E0ULL;
    *(uint32_t *)(v_rip + 0x3A3B77) = 1;
    return v_rip + 3816353;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C1EFA8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C1EFA8[BB_00C1EFA8]
  bb_00C1EFDA[BB_00C1EFDA]
```
