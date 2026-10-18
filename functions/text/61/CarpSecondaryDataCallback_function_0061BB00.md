# CarpSecondaryDataCallback

- RVA: `0x0061BB00`–`0x0061BB24` (길이 `36` bytes)
- VA: `0x000000014061BB00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `36/36` bytes 표시
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
- `0x0061BB00` → RVA `0x00038328` (`.rdata`; read)
- `0x0061BB0D` → RVA `0x00F02504` (`.data`; read)
- `0x0061BB17` → RVA `0x00F02500` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061BB00  0F 10 05 21 C8 A1 FF            movups xmm0, xmmword ptr [rip - 0x5e37df]
0061BB07  F3 41 0F 7F 40 10               movdqu xmmword ptr [r8 + 0x10], xmm0
0061BB0D  8B 05 F1 69 8E 00               mov eax, dword ptr [rip + 0x8e69f1]
0061BB13  41 89 40 28                     mov dword ptr [r8 + 0x28], eax
0061BB17  48 8D 05 E2 69 8E 00            lea rax, [rip + 0x8e69e2]
0061BB1E  49 89 40 20                     mov qword ptr [r8 + 0x20], rax
0061BB22  C3                              ret
0061BB23  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CarpSecondaryDataCallback(__int64 a1, __int64 a2, __int64 a3)
{
    *(unsigned __int64 *)(a3 + 16) = v_xmm0;
    *(unsigned int *)(a3 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9333233)));
    *(unsigned __int64 *)(a3 + 32) = v_rip + 9333218;
    return v_rip + 9333218;
}
```

## 5. (Beta) C Style

```c
int64_t CarpSecondaryDataCallback(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    *(uint64_t *)(arg3 + 0x10) = v_xmm0;
    *(uint32_t *)(arg3 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8E69F1)));
    *(uint64_t *)(arg3 + 0x20) = v_rip + 9333218;
    return v_rip + 9333218;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x10` | `128` | `W` |
| `Arg3` | `+ 0x20` | `64` | `W` |
| `Arg3` | `+ 0x28` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061BB00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061BB00[BB_0061BB00]
  bb_0061BB23[BB_0061BB23]
```
