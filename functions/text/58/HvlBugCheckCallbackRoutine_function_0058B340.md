# HvlBugCheckCallbackRoutine

- RVA: `0x0058B340`–`0x0058B37A` (길이 `58` bytes)
- VA: `0x000000014058B340`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `15`개 명령, `58/58` bytes 표시
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
- `0x0058B340` → RVA `0x00F8ED88` (`.data`; read)
- `0x0058B353` → RVA `0x00026908` (`.rdata`; read)
- `0x0058B36B` → RVA `0x00F8ED98` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058B340  48 8B 05 41 3A A0 00            mov rax, qword ptr [rip + 0xa03a41]
0058B347  48 85 C0                        test rax, rax
0058B34A  74 2C                           je 0x14058b378
0058B34C  8B 40 04                        mov eax, dword ptr [rax + 4]
0058B34F  A8 01                           test al, 1
0058B351  74 25                           je 0x14058b378
0058B353  0F 10 05 AE B5 A9 FF            movups xmm0, xmmword ptr [rip - 0x564a52]
0058B35A  F3 41 0F 7F 40 10               movdqu xmmword ptr [r8 + 0x10], xmm0
0058B360  48 8B 05 21 3A A0 00            mov rax, qword ptr [rip + 0xa03a21]
0058B367  49 89 40 20                     mov qword ptr [r8 + 0x20], rax
0058B36B  8B 05 27 3A A0 00               mov eax, dword ptr [rip + 0xa03a27]
0058B371  C1 E0 0C                        shl eax, 0xc
0058B374  41 89 40 28                     mov dword ptr [r8 + 0x28], eax
0058B378  C3                              ret
0058B379  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlBugCheckCallbackRoutine(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    if (*(unsigned __int64 *)(v_rip + 10500673) == 0) goto loc_0058B378;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10500673) + 4));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10500673) + 4)))) & (1)) != 0) {
        *(unsigned __int64 *)(a3 + 16) = v_xmm0;
        result = *(unsigned __int64 *)(v_rip + 10500641);
        *(unsigned __int64 *)(a3 + 32) = result;
        result = *(unsigned int *)(v_rip + 10500647);
        result = (unsigned int)((result) << (12));
        *(unsigned int *)(a3 + 40) = (unsigned int)(result);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlBugCheckCallbackRoutine(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    if (*(uint64_t *)(v_rip + 0xA03A41) == 0) goto loc_0058B378;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA03A41) + 0x4));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA03A41) + 0x4)))) & (1)) != 0) {
        *(uint64_t *)(arg3 + 0x10) = v_xmm0;
        result = *(uint64_t *)(v_rip + 0xA03A21);
        *(uint64_t *)(arg3 + 0x20) = result;
        result = *(uint32_t *)(v_rip + 0xA03A27);
        result = (uint32_t)((result) << (12));
        *(uint32_t *)(arg3 + 0x28) = (uint32_t)(result);
    }
    return result;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058B340&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058B340[BB_0058B340]
  bb_0058B34C[BB_0058B34C]
  bb_0058B353[BB_0058B353]
  bb_0058B378[BB_0058B378]
  bb_0058B379[BB_0058B379]
  bb_0058B340 -->|branch| bb_0058B378
  bb_0058B340 -->|fallthrough| bb_0058B34C
  bb_0058B34C -->|branch| bb_0058B378
  bb_0058B34C -->|fallthrough| bb_0058B353
  bb_0058B353 -->|flow| bb_0058B378
```
