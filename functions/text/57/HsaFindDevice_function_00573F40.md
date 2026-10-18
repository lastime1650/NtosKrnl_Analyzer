# HsaFindDevice

- RVA: `0x00573F40`–`0x00573F67` (길이 `39` bytes)
- VA: `0x0000000140573F40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `15`개 명령, `39/39` bytes 표시
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
00573F40  83 3A 01                        cmp dword ptr [rdx], 1
00573F43  75 1E                           jne 0x140573f63
00573F45  44 0F B7 42 08                  movzx r8d, word ptr [rdx + 8]
00573F4A  44 39 81 A0 00 00 00            cmp dword ptr [rcx + 0xa0], r8d
00573F51  75 10                           jne 0x140573f63
00573F53  4D 85 C9                        test r9, r9
00573F56  74 07                           je 0x140573f5f
00573F58  0F B7 4A 0C                     movzx ecx, word ptr [rdx + 0xc]
00573F5C  49 89 09                        mov qword ptr [r9], rcx
00573F5F  B0 01                           mov al, 1
00573F61  C3                              ret
00573F62  CC                              int3
00573F63  32 C0                           xor al, al
00573F65  C3                              ret
00573F66  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HsaFindDevice(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;

    if ((*(unsigned int *)(a2)) != 1) goto loc_00573F63;
    if ((*(unsigned int *)(a1 + 160)) != ((unsigned int)(*(unsigned __int16 *)(a2 + 8)))) goto loc_00573F63;
    if (a4 != 0) {
        a1 = *(unsigned __int16 *)(a2 + 12);
        *(unsigned __int64 *)(a4) = a1;
    }
    return 1;
loc_00573F63:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HsaFindDevice(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint32_t *)(arg2)) != 1) goto loc_00573F63;
    if ((*(uint32_t *)(arg1 + 0xA0)) != ((uint32_t)(*(uint16_t *)(arg2 + 0x8)))) goto loc_00573F63;
    if (Arg4 != 0) {
        Arg1 = *(uint16_t *)(arg2 + 0xC);
        *(void **)(Arg4) = Arg1;
    }
    return 1;
loc_00573F63:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xA0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x8` | `16` | `R` |
| `Arg2` | `+ 0xC` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00573F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00573F40[BB_00573F40]
  bb_00573F45[BB_00573F45]
  bb_00573F53[BB_00573F53]
  bb_00573F58[BB_00573F58]
  bb_00573F5F[BB_00573F5F]
  bb_00573F62[BB_00573F62]
  bb_00573F63[BB_00573F63]
  bb_00573F66[BB_00573F66]
  bb_00573F40 -->|branch| bb_00573F63
  bb_00573F40 -->|fallthrough| bb_00573F45
  bb_00573F45 -->|branch| bb_00573F63
  bb_00573F45 -->|fallthrough| bb_00573F53
  bb_00573F53 -->|branch| bb_00573F5F
  bb_00573F53 -->|fallthrough| bb_00573F58
  bb_00573F58 -->|flow| bb_00573F5F
  bb_00573F62 -->|flow| bb_00573F63
```
