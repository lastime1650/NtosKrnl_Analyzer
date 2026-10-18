# ExQueryTimerResolution

- RVA: `0x004AF7B0`–`0x004AF7CB` (길이 `27` bytes)
- VA: `0x00000001404AF7B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004AF7B0` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x004AF7B8` → RVA `0x00FC6B3C` (`ALMOSTRO`; read)
- `0x004AF7C0` → RVA `0x00FC6BB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004AF7B0  8B 05 EA 72 B1 00               mov eax, dword ptr [rip + 0xb172ea]
004AF7B6  89 01                           mov dword ptr [rcx], eax
004AF7B8  8B 05 7E 73 B1 00               mov eax, dword ptr [rip + 0xb1737e]
004AF7BE  89 02                           mov dword ptr [rdx], eax
004AF7C0  8B 05 F2 73 B1 00               mov eax, dword ptr [rip + 0xb173f2]
004AF7C6  41 89 00                        mov dword ptr [r8], eax
004AF7C9  C3                              ret
004AF7CA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExQueryTimerResolution(__int64 a1, __int64 a2, __int64 a3)
{
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11629290)));
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11629438)));
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11629554)));
    return (unsigned int)(*(unsigned int *)(v_rip + 11629554));
}
```

## 5. (Beta) C Style

```c
int64_t ExQueryTimerResolution(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB172EA)));
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB1737E)));
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB173F2)));
    return (uint32_t)(*(uint32_t *)(v_rip + 0xB173F2));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004AF7B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004AF7B0[BB_004AF7B0]
  bb_004AF7CA[BB_004AF7CA]
```
