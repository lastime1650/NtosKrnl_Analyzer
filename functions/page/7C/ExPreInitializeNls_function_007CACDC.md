# ExPreInitializeNls

- RVA: `0x007CACDC`–`0x007CAD11` (길이 `53` bytes)
- VA: `0x00000001407CACDC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [InitBootProcessor](../../init/C1/InitBootProcessor_function_00C1B1C8.md) at `0x00C1B400`

### Static image references
- `0x007CACDC` → RVA `0x01008190` (`INITDATA`; read)
- `0x007CACEC` → RVA `0x00FCFDF0` (`CACHEALI`; read/write)
- `0x007CACFF` → RVA `0x00FCFDF8` (`CACHEALI`; read/write)
- `0x007CAD06` → RVA `0x00FCFDE8` (`CACHEALI`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007CACDC  48 8B 15 AD D4 83 00            mov rdx, qword ptr [rip + 0x83d4ad]
007CACE3  48 85 D2                        test rdx, rdx
007CACE6  74 25                           je 0x1407cad0d
007CACE8  48 8D 42 04                     lea rax, [rdx + 4]
007CACEC  48 87 05 FD 50 80 00            xchg qword ptr [rip + 0x8050fd], rax
007CACF3  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
007CACF7  48 83 C0 02                     add rax, 2
007CACFB  48 8D 04 42                     lea rax, [rdx + rax*2]
007CACFF  48 87 05 F2 50 80 00            xchg qword ptr [rip + 0x8050f2], rax
007CAD06  48 89 15 DB 50 80 00            mov qword ptr [rip + 0x8050db], rdx
007CAD0D  33 C0                           xor eax, eax
007CAD0F  C3                              ret
007CAD10  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExPreInitializeNls(void)
{
    __int64 result;

    if (*(unsigned __int64 *)(v_rip + 8639661) != 0) {
        result = *(unsigned __int64 *)(v_rip + 8639661) + 4;
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8639661) + 2);
        result = (result) + (2);
        result = *(unsigned __int64 *)(v_rip + 8639661) + result * 2;
        *(unsigned __int64 *)(v_rip + 8409307) = *(unsigned __int64 *)(v_rip + 8639661);
    }
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
void ExPreInitializeNls(void)
{
    int64_t result;

    if (*(uint64_t *)(v_rip + 0x83D4AD) != 0) {
        result = *(uint64_t *)(v_rip + 0x83D4AD) + 4;
        result = *(uint16_t *)(*(uint64_t *)(v_rip + 0x83D4AD) + 0x2);
        result = (result) + (2);
        result = *(uint64_t *)(v_rip + 0x83D4AD) + result * 2;
        *(uint64_t *)(v_rip + 0x8050DB) = *(uint64_t *)(v_rip + 0x83D4AD);
    }
    result = 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007CACDC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007CACDC[BB_007CACDC]
  bb_007CACE8[BB_007CACE8]
  bb_007CAD0D[BB_007CAD0D]
  bb_007CAD10[BB_007CAD10]
  bb_007CACDC -->|branch| bb_007CAD0D
  bb_007CACDC -->|fallthrough| bb_007CACE8
  bb_007CACE8 -->|flow| bb_007CAD0D
```
