# FsRtlIsDaxVolume

- RVA: `0x00581080`–`0x005810A0` (길이 `32` bytes)
- VA: `0x0000000140581080`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `32/32` bytes 표시
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
00581080  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00581084  48 85 C0                        test rax, rax
00581087  74 13                           je 0x14058109c
00581089  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0058108D  48 85 C0                        test rax, rax
00581090  74 0A                           je 0x14058109c
00581092  8B 40 30                        mov eax, dword ptr [rax + 0x30]
00581095  C1 E8 1C                        shr eax, 0x1c
00581098  24 01                           and al, 1
0058109A  C3                              ret
0058109B  CC                              int3
0058109C  32 C0                           xor al, al
0058109E  C3                              ret
0058109F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlIsDaxVolume(__int64 a1)
{
    __int64 result;

    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_0058109C;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) == 0) goto loc_0058109C;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8) + 48))) >> (28));
    result = (unsigned __int8)((result) & (1));
    return result;
loc_0058109C:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlIsDaxVolume(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_0058109C;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) == 0) goto loc_0058109C;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8) + 0x30))) >> (28));
    result = (uint8_t)((result) & (1));
    return result;
loc_0058109C:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00581080&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00581080[BB_00581080]
  bb_00581089[BB_00581089]
  bb_00581092[BB_00581092]
  bb_0058109B[BB_0058109B]
  bb_0058109C[BB_0058109C]
  bb_0058109F[BB_0058109F]
  bb_00581080 -->|branch| bb_0058109C
  bb_00581080 -->|fallthrough| bb_00581089
  bb_00581089 -->|branch| bb_0058109C
  bb_00581089 -->|fallthrough| bb_00581092
  bb_0058109B -->|flow| bb_0058109C
```
