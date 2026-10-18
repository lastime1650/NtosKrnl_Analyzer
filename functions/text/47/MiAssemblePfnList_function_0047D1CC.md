# MiAssemblePfnList

- RVA: `0x0047D1CC`–`0x0047D1FB` (길이 `47` bytes)
- VA: `0x000000014047D1CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `15`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiProcessPageGroupInfo](../37/MiProcessPageGroupInfo_function_00376910.md) at `0x00376965`
- [sub_006E75BA](../6E/Unknown_function_006E75BA.md) at `0x006E76C9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047D1CC  41 8B C0                        mov eax, r8d
0047D1CF  4C 8D 04 40                     lea r8, [rax + rax*2]
0047D1D3  4A 8D 04 C1                     lea rax, [rcx + r8*8]
0047D1D7  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0047D1DB  48 39 01                        cmp qword ptr [rcx], rax
0047D1DE  74 07                           je 0x14047d1e7
0047D1E0  B9 03 00 00 00                  mov ecx, 3
0047D1E5  CD 29                           int 0x29
0047D1E7  48 89 02                        mov qword ptr [rdx], rax
0047D1EA  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
0047D1EE  48 89 11                        mov qword ptr [rcx], rdx
0047D1F1  48 89 50 08                     mov qword ptr [rax + 8], rdx
0047D1F5  48 FF 40 10                     inc qword ptr [rax + 0x10]
0047D1F9  C3                              ret
0047D1FA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAssemblePfnList(__int64 a1, __int64 a2, int a3)
{
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + (unsigned int)(a3) + (unsigned int)(a3) * 2 * 8 + 8))) != (a1 + (unsigned int)(a3) + (unsigned int)(a3) * 2 * 8)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(a2) = a1 + (unsigned int)(a3) + (unsigned int)(a3) * 2 * 8;
    *(unsigned __int64 *)(a2 + 8) = a1;
    *(unsigned __int64 *)(a1) = a2;
    *(unsigned __int64 *)(a1 + (unsigned int)(a3) + (unsigned int)(a3) * 2 * 8 + 8) = a2;
    return a1 + (unsigned int)(a3) + (unsigned int)(a3) * 2 * 8;
}
```

## 5. (Beta) C Style

```c
int64_t MiAssemblePfnList(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    if ((*(uint64_t *)(*(uint64_t *)(arg1 + (uint32_t)(arg3) + (uint32_t)(arg3) * 2 * 8 + 0x8))) != (Arg1 + (uint32_t)(Arg3) + (uint32_t)(Arg3) * 2 * 8)) {
        Arg1 = 3;
    }
    *(void **)(arg2) = Arg1 + (uint32_t)(Arg3) + (uint32_t)(Arg3) * 2 * 8;
    *(void **)(arg2 + 0x8) = Arg1;
    *(void **)(arg1) = Arg2;
    *(void **)(arg1 + (uint32_t)(arg3) + (uint32_t)(arg3) * 2 * 8 + 0x8) = Arg2;
    return Arg1 + (uint32_t)(Arg3) + (uint32_t)(Arg3) * 2 * 8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + r8*8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x10` | `64` | `R/W` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x0 + rax*2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047D1CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047D1CC[BB_0047D1CC]
  bb_0047D1E0[BB_0047D1E0]
  bb_0047D1E7[BB_0047D1E7]
  bb_0047D1FA[BB_0047D1FA]
  bb_0047D1CC -->|branch| bb_0047D1E7
  bb_0047D1CC -->|fallthrough| bb_0047D1E0
  bb_0047D1E0 -->|flow| bb_0047D1E7
```
