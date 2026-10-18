# rand

- RVA: `0x005011F0`–`0x0050120F` (길이 `31` bytes)
- VA: `0x00000001405011F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `31/31` bytes 표시
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
- `0x005011F0` → RVA `0x00E0A680` (`.data`; read)
- `0x005011FF` → RVA `0x00E0A680` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005011F0  69 05 86 94 90 00 FD 43 03 00   imul eax, dword ptr [rip + 0x909486], 0x343fd
005011FA  05 C3 9E 26 00                  add eax, 0x269ec3
005011FF  89 05 7B 94 90 00               mov dword ptr [rip + 0x90947b], eax
00501205  C1 F8 10                        sar eax, 0x10
00501208  25 FF 7F 00 00                  and eax, 0x7fff
0050120D  C3                              ret
0050120E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall rand(void)
{
    __int64 result;

    result = (unsigned int)((result) * (*(unsigned int *)(v_rip + 9475206)));
    result = (unsigned int)((result) + (0x269EC3ULL));
    *(unsigned int *)(v_rip + 9475195) = (unsigned int)(result);
    result = (unsigned int)((result) >> (16));
    result = (unsigned int)((result) & (0x7FFFULL));
    return result;
}
```

## 5. (Beta) C Style

```c
void rand(void)
{
    int64_t result;

    result = (uint32_t)((result) * (*(uint32_t *)(v_rip + 0x909486)));
    result = (uint32_t)((result) + (0x269EC3ULL));
    *(uint32_t *)(v_rip + 0x90947B) = (uint32_t)(result);
    result = (uint32_t)((result) >> (16));
    result = (uint32_t)((result) & (0x7FFFULL));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005011F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005011F0[BB_005011F0]
  bb_0050120E[BB_0050120E]
```
