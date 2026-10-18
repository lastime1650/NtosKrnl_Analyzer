# SmBugcheckCallback

- RVA: `0x00610370`–`0x006103A3` (길이 `51` bytes)
- VA: `0x0000000140610370`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `15`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00610370` → RVA `0x00E28938` (`.data`; read)
- `0x0061038A` → RVA `0x00038040` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00610370  48 8B 15 C1 85 81 00            mov rdx, qword ptr [rip + 0x8185c1]
00610377  33 C9                           xor ecx, ecx
00610379  48 85 D2                        test rdx, rdx
0061037C  74 1F                           je 0x14061039d
0061037E  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
00610381  83 C0 38                        add eax, 0x38
00610384  41 3B 40 0C                     cmp eax, dword ptr [r8 + 0xc]
00610388  77 13                           ja 0x14061039d
0061038A  0F 10 05 AF 7C A2 FF            movups xmm0, xmmword ptr [rip - 0x5d8351]
00610391  49 89 50 20                     mov qword ptr [r8 + 0x20], rdx
00610395  8B C8                           mov ecx, eax
00610397  F3 41 0F 7F 40 10               movdqu xmmword ptr [r8 + 0x10], xmm0
0061039D  41 89 48 28                     mov dword ptr [r8 + 0x28], ecx
006103A1  C3                              ret
006103A2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SmBugcheckCallback(int a1, __int64 a2, __int64 a3)
{
    __int64 result;

    a1 = 0;
    if (*(unsigned __int64 *)(v_rip + 8488385) == 0) goto loc_0061039D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 8488385) + 12))) + (56));
    if (((unsigned int)(result)) <= (*(unsigned int *)(a3 + 12))) {
        *(unsigned __int64 *)(a3 + 32) = *(unsigned __int64 *)(v_rip + 8488385);
        a1 = (unsigned int)(result);
        *(unsigned __int64 *)(a3 + 16) = v_xmm0;
    }
    *(unsigned int *)(a3 + 40) = a1;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SmBugcheckCallback(int32_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    Arg1 = 0;
    if (*(uint64_t *)(v_rip + 0x8185C1) == 0) goto loc_0061039D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x8185C1) + 0xC))) + (56));
    if (((uint32_t)(result)) <= (*(uint32_t *)(arg3 + 0xC))) {
        *(uint64_t *)(arg3 + 0x20) = *(uint64_t *)(v_rip + 0x8185C1);
        Arg1 = (uint32_t)(result);
        *(uint64_t *)(arg3 + 0x10) = v_xmm0;
    }
    *(uint32_t *)(arg3 + 0x28) = Arg1;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0xC` | `32` | `R` |
| `Arg3` | `+ 0x10` | `128` | `W` |
| `Arg3` | `+ 0x20` | `64` | `W` |
| `Arg3` | `+ 0x28` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00610370&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00610370[BB_00610370]
  bb_0061037E[BB_0061037E]
  bb_0061038A[BB_0061038A]
  bb_0061039D[BB_0061039D]
  bb_006103A2[BB_006103A2]
  bb_00610370 -->|branch| bb_0061039D
  bb_00610370 -->|fallthrough| bb_0061037E
  bb_0061037E -->|branch| bb_0061039D
  bb_0061037E -->|fallthrough| bb_0061038A
  bb_0061038A -->|flow| bb_0061039D
```
