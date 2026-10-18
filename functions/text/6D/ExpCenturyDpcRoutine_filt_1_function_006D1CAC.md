# ExpCenturyDpcRoutine$filt$1

- RVA: `0x006D1CAC`–`0x006D1CD0` (길이 `36` bytes)
- VA: `0x00000001406D1CAC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005F7D4`
- 디코드: `14`개 명령, `36/36` bytes 표시
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
006D1CAC  40 55                           push rbp
006D1CAE  48 83 EC 30                     sub rsp, 0x30
006D1CB2  48 8B EA                        mov rbp, rdx
006D1CB5  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D1CB8  83 C0 02                        add eax, 2
006D1CBB  89 45 30                        mov dword ptr [rbp + 0x30], eax
006D1CBE  8B 4D 30                        mov ecx, dword ptr [rbp + 0x30]
006D1CC1  33 C0                           xor eax, eax
006D1CC3  83 F9 02                        cmp ecx, 2
006D1CC6  0F 94 C0                        sete al
006D1CC9  48 83 C4 30                     add rsp, 0x30
006D1CCD  5D                              pop rbp
006D1CCE  C3                              ret
006D1CCF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpCenturyDpcRoutine_filt_1(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 48))) + (2));
    *(unsigned int *)(a2 + 48) = (unsigned int)(result);
    result = 0;
    result = (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48)))) == 2) ? 1 : 0;
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpCenturyDpcRoutine_filt_1(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x30))) + (2));
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
    result = 0;
    result = (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30)))) == 2) ? 1 : 0;
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D1CAC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D1CAC[BB_006D1CAC]
  bb_006D1CCF[BB_006D1CCF]
```
